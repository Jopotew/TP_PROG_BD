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
                    




       