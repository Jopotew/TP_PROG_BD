from supabase import create_client, Client


class DataBase():
    def __init__(self):
        self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkZmx1a3lvc3NiZXVwaHlldWZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjgzMDA1NTgsImV4cCI6MjA0Mzg3NjU1OH0.lkUwkPifUMKOcJSu-ODIaZQZmtK4HTsq9ruWWSLnF6g"  
        self.url = "https://rdflukyossbeuphyeufp.supabase.co"
        self.database: Client = create_client(self.url, self.key)

    def search_by_row(self, table, row):  # BUSCA POR FILA
        row_to_search = self.database.table(table).select(row).execute()
        return row_to_search.data
    
    def search_by_row_and_key(self, table, row, column, key_to_search):  # BUSCA POR FILA
        row_to_search = self.database.table(table).select(row).eq(column, key_to_search).execute()
        return row_to_search.data
    
    def search_by_product(self, table, product):  # BUSCA UN PRODUCTO
        product_to_search = self.database.table(table).select("ID, producto, stock").eq("producto", product).execute()
        return product_to_search.data
    
    def search_username(self, table, username):  #Busca contrasenias
        product_to_search = self.database.table(table).select("ID, USERNAME, PASSWORD").eq("USERNAME", username).execute()
        return product_to_search.data

    def insert_product(self, table, data):  # INSERTA UN PRODUCTO
        response = self.database.table(table).insert(data).execute()
        return response.data

    def update_product(self, table, product_id, data):  
        """ 
        MODIFICA UN PRODUCTO. DEBE RECIBIR UN DICT. EJEMPLO : DATA_A_CAMBIAR = {"STOCK" : 3}
        PUEDE TAMBIEN RECIBIR OTRA COSA. EJ: DATA_A_CAMBIAR = {"NOMBRE_PRODUCTO" : "MANZANA"}
        LA PRIMERA PARTE DEL DICT REFIERE A LA SECCION DE LA TABLA QUE QUERES MODIFICAR
        """
        response = self.database.table(table).update(data).eq('id', product_id).execute()
        return response.data

    def delete_product(self, table, product_id):  # ELIMINA UN PRODUCTO
        response = self.database.table(table).delete().eq('id', product_id).execute()
        return response.data
                    
                        
    def check_and_create_order(self, username):
        
        client_info = self.search_username("CLIENT", username)
        if not client_info:
            print(f"Cliente con username '{username}' no encontrado.")
            return None
        
        client_id = client_info[0]['ID']
        client_order = self.search_by_row_and_key("ORDER", "*", "ID_CLIENT", client_id)
        
        if client_order:
            for status in client_order:
                if status["ID_STATUS"] == 1: 
                    print("EXISTE ORDEN PAGA")
                    for unpaid_status in client_order:
                        print("BUSCANDO ORDEN IMPAGA")
                        if unpaid_status["ID_STATUS"] == 2:
                            print("hay una orden paga, pero tiene una impaga. Utilizando la impaga")
                            unpaid_order = self.return_unpaid_order(client_id, username)
                            return unpaid_order
                    print("NO EXISTE ORDEN IMPAGA")
                    new_order = self.create_new_order(client_id, username)   
                    return new_order   
                            
                else:   
                    print("ORden impaga")
                    unpaid_order = self.return_unpaid_order(client_id, username)
                    return unpaid_order

        else:       
            print("NO HAY ORDEN")
            new_order = self.create_new_order(client_id, username)   
            return new_order   
    
    def return_unpaid_order(self, client_id, username):
        existing_order = self.database.table("ORDER").select("*").eq("ID_CLIENT", client_id).eq("ID_STATUS", 2).execute()
        if existing_order.data:
            print(f"Orden existente encontrada para el cliente '{username}'.")
            print("RETURNS UNPAID ORDER")
            return existing_order.data[0] 
        
    def create_new_order(self, client_id, username):
        new_order_data = {
        "ID_CLIENT": client_id,
        "ID_STATUS": 2,
        "TOTAL_ORDER": 0,
            }
        new_order = self.insert_product("ORDER", new_order_data)
        print(f"Se ha creado una nueva orden para el cliente '{username}'.")
        print("CREATES NEW ORDER")
        return new_order

#Queda hacer que se ligue a una orderLine
    def new_order_line(self, order, product):
        order_id = order[0]["ID"]
        product_table= self.search_by_row_and_key("PRODUCT","*","NAME",product)
        product_id = product_table[0]["ID"]
        order_line_table = self.search_by_row_key("ORDER_LINE","*","ID_PRODUCT", product_id)

        for order in order_line_table:
            quantity = order["QUANTITY"]
            if product_id == order["ID_PRODUCT"] & order_id == order["ID_ORDER"]:
                print("ID PRODUCTO Y ID ORDER ENCONTRADOS DENTRO DEL ORDERLINE")
                print("SUMANDO 1 A LA CANTIDAD")
                self.create_order_line(product_id, order_id, quantity)
            else : 
                print("ID PRODUCTO NO EXISTE DENTRO DEL ORDERLINE")
                print("CREANDO  NUEVO ORDERLINE CON PRODUCTO")
                self.create_order_line(product_id, order_id, quantity)
        print("No hay ordenes dentro de la orderline, creando una")
        quantity = order_line_table[0]["QUANTITY"]
        self.create_order_line(product_id, order_id, quantity)


    def create_order_line(self, product_id, order_id, quantity):
        new_order_line_data : dict = {
            "ID_PRODUCT": product_id,
            "ID_ORDER" : order_id,
            "QUANTITY": quantity + 1,
            }
        new_line = self.insert_product("ORDER_LINE", new_order_line_data)
        return new_line
        


        



db = DataBase()



def test():
    order = db.check_and_create_order("UserMigue")
    db.new_order_line("Queso", order)

test()