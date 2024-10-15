from supabase import create_client, Client


class DataBase():
    def __init__(self):
        self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkZmx1a3lvc3NiZXVwaHlldWZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjgzMDA1NTgsImV4cCI6MjA0Mzg3NjU1OH0.lkUwkPifUMKOcJSu-ODIaZQZmtK4HTsq9ruWWSLnF6g"  
        self.url = "https://rdflukyossbeuphyeufp.supabase.co"
        self.database: Client = create_client(self.url, self.key)

    def search_by_row_key(self, table, row):  # BUSCA POR FILA
        row_to_search = self.database.table(table).select(row).execute()
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
        payed = 1
        not_payed = 2
        if not client_info:
            print(f"Cliente con username '{username}' no encontrado.")
            return None
        
        client_id = client_info[0]['ID']
        
        client_order = self.database.table("ORDER").select("*").eq("ID_CLIENT", client_id).execute()
        
        #FALTA HACER QUE BUSQUE SI HAY UNA IMPAGA.

        if client_order.data:
            
            unpayed_status = self.database.table("ORDER").select("*").eq("ID_CLIENT", client_id).eq("ID_STATUS", not_payed).execute()
            
            payed_status =  self.database.table("ORDER").select("*").eq("ID_CLIENT", client_id).eq("ID_STATUS", payed).execute()
            
            if payed_status.data[0]["ID_STATUS"] == 1:
                print(username,"tiene una orden paga, se creara una nueva. ")
                new_order_data = {
                "ID_CLIENT": client_id,
                "ID_STATUS": 2,
                "TOTAL_ORDER": 0,
                 }
                new_order = self.insert_product("ORDER", new_order_data)
                print(f"Se ha creado una nueva orden para el cliente '{username}'.")
                return new_order
            
            if unpayed_status.data[0]["ID_STATUS"] == 2:
                existing_order = self.database.table("ORDER").select("*").eq("ID_CLIENT", client_id).eq("ID_STATUS", 2).execute()
                if existing_order.data:
                    print(existing_order)
                    print(f"Orden existente encontrada para el cliente '{username}'.")
                    return existing_order.data[0]  
            
        else:       
            new_order_data = {
                "ID_CLIENT": client_id,
                "ID_STATUS": 2,
                "TOTAL_ORDER": 0,
            }
            
            new_order = self.insert_product("ORDER", new_order_data)
            print(f"Se ha creado una nueva orden para el cliente '{username}'.")
            return new_order



db = DataBase()

db.check_and_create_order("UserMigue")