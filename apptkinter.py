import customtkinter as ctk
from conexaoDB import conexao
from mysql.connector import Error

condb = conexao()


class Aplicacao():
    
    def __init__(self):
        self.janela = ctk.CTk()
        self.tela()
        self.frame_telaInicial()
        self.janela.mainloop()
        
    def tela(self):
        self.janela.title("App teste")
        self.janela.geometry("700x400") 
        self.janela.resizable(False, False) 
        self.janela._set_appearance_mode("system")
    
    def frame_telaInicial(self):
        frame_telaInicial = ctk.CTkFrame(master= self.janela, width=680, height= 380)
        frame_telaInicial.place(x= 10, y= 10)
        
        label_bemvindo = ctk.CTkLabel(master= frame_telaInicial, text= "SEJA BEM-VINDO", font=("Roboto", 24), width= 20)
        label_bemvindo.place(x= 219, y= 20)
        
        label_opc = ctk.CTkLabel(master= frame_telaInicial, text= "APERTE UMA OPÇÃO:").place(x= 30, y= 60)
        
        btn_Cadastrar = ctk.CTkButton(master= frame_telaInicial, text= "Cadastrar", width= 5, height= 10, command= lambda: (self.cadastros(), self.janela.withdraw())).place(x= 30, y= 100)
        
        btn_Alterar = ctk.CTkButton(master= frame_telaInicial, text= "Alterar", width= 5, height= 10).place(x= 30, y= 130)

        btn_Deletar = ctk.CTkButton(master= frame_telaInicial, text= "Deletar", width= 5, height= 10).place(x= 30, y= 160)
       
    def cadastros(self):
        
        self.janela.iconify()
        self.janela_cadastro = ctk.CTkToplevel(self.janela)
        self.janela_cadastro.title("CADASTROS")
        self.janela_cadastro.geometry("500x500")
        self.janela_cadastro.resizable(False, False)
            
        self.btn_cadastrarCliente = ctk.CTkButton(master= self.janela_cadastro, text= "Cadastrar cliente", command= lambda: (self.frame_cadastroCliente())).pack(pady= 20)
        self.btn_cadastrarFornecedor = ctk.CTkButton(master= self.janela_cadastro, text= "Cadastrar fornecedor", command= lambda: (self.frame_cadastroFornecedor())).pack(pady= 21)
        self.btn_voltar = ctk.CTkButton(master= self.janela_cadastro, text= "VOLTAR", command= lambda: (self.janela_cadastro.destroy(), self.janela.deiconify())).pack(pady= 80)
            
        
        
    def frame_cadastroCliente(self):
        self.frameCliente = ctk.CTkFrame(master= self.janela_cadastro, width= 480, height= 480, fg_color="teal")
        self.frameCliente.place(x= 10, y= 10)
        
        self.nomeCli = ctk.CTkLabel(master= self.frameCliente, text= "*Nome:", bg_color= "teal", width= 20).place(x= 20, y= 20)
        self.entry_nomeCli = ctk.CTkEntry(master= self.frameCliente, bg_color= "teal", width= 200)
        self.entry_nomeCli.place(x= 110, y= 20)
        
        self.sobrenomeCli = ctk.CTkLabel(master= self.frameCliente, text= "*Sobrenome:", bg_color= "teal", width= 20).place(x= 20, y= 70)
        self.entry_sobrenomeCli = ctk.CTkEntry(master= self.frameCliente, bg_color= "teal", width= 200)
        self.entry_sobrenomeCli.place(x= 110, y= 70)
        
        self.enderecoCli = ctk.CTkLabel(master= self.frameCliente, text= "*Endereço:", bg_color= "teal", width= 20).place(x= 20, y= 120)
        self.entry_enderecoCli = ctk.CTkEntry(master= self.frameCliente, bg_color= "teal", width= 200)
        self.entry_enderecoCli.place(x= 110, y= 120)
        
        self.cidadeCli = ctk.CTkLabel(master= self.frameCliente, text= "*Cidade:", bg_color= "teal", width= 20).place(x= 20, y= 170)
        self.entry_cidadeCli = ctk.CTkEntry(master= self.frameCliente, bg_color= "teal", width= 200)
        self.entry_cidadeCli.place(x= 110, y= 170)
        
        self.CodigoPostalCli = ctk.CTkLabel(master= self.frameCliente, text= "*Codigo Postal:", bg_color= "teal", width= 20).place(x= 20, y= 220)
        self.entry_CodigoPostalCli = ctk.CTkEntry(master= self.frameCliente, bg_color= "teal", width= 200)
        self.entry_CodigoPostalCli.place(x= 110, y= 220)     
        
        self.btn_enviar = ctk.CTkButton(master= self.frameCliente, text= "ENVIAR", width= 50, bg_color= "teal", command=self.cadastrarCliente).place(x= 50, y= 400)
        self.btn_quit = ctk.CTkButton(master= self.frameCliente, text= "FECHAR", width= 50, bg_color= "teal", command= lambda:(self.frameCliente.destroy(), self.janela_cadastro.deiconify())).place(x= 120, y= 400)
        
    def frame_cadastroFornecedor(self):
        
        self.frameFornecedor = ctk.CTkFrame(master= self.janela_cadastro, width= 480, height= 480, fg_color="teal")
        self.frameFornecedor.place(x= 10, y= 10)
        
        self.label_nomeForn = ctk.CTkLabel(master= self.frameFornecedor, text= "Nome:", bg_color= "teal", width= 20).place(x= 20, y= 20)
        self.entry_nomeForn = ctk.CTkEntry(master= self.frameFornecedor, bg_color= "teal", width= 200)
        self.entry_nomeForn.place(x= 60, y= 20)
        
        self.label_contatoForn = ctk.CTkLabel(master= self.frameFornecedor, text= "Contato:", bg_color= "teal", width= 20).place(x= 20, y= 70)
        self.entry_contatoForn = ctk.CTkEntry(master= self.frameFornecedor,bg_color= "teal", width= 200)
        self.entry_contatoForn.place(x= 70, y= 70)

        self.label_enderecoForn = ctk.CTkLabel(master= self.frameFornecedor, text= "Endereço:", bg_color= "teal", width= 20).place(x= 20, y= 120)
        self.entry_enderecoForn = ctk.CTkEntry(master= self.frameFornecedor, bg_color= "teal", width= 200)
        self.entry_enderecoForn.place(x= 80, y= 120)
        
        self.btn_enviar = ctk.CTkButton(master= self.frameFornecedor, text= "ENVIAR", width= 50, bg_color= "teal", command=self.cadastrarFornecedor).place(x= 20, y= 340)
        self.btn_quit = ctk.CTkButton(master= self.frameFornecedor, text= "FECHAR", width= 50, bg_color= "teal", command= lambda:(self.frameFornecedor.destroy(), self.janela_cadastro.deiconify())).place(x= 20, y= 380)
            
            
        
    def cadastrarFornecedor(self):
            nome = self.entry_nomeForn.get()
            contato = self.entry_contatoForn.get()
            endereco = self.entry_enderecoForn.get()
            
            mycursor = condb.cursor()
            sql = 'INSERT INTO fornecedores (Nome, Contato, Endereco) VALUES (%s, %s, %s);'
            valores = (nome, contato, endereco)

            try: 
                mycursor.execute(sql, valores)
                condb.commit()
                self.entry_nomeForn.delete(0, 'end')
                self.entry_contatoForn.delete(0, 'end')
                self.entry_enderecoForn.delete(0, 'end')
                label_sucesso = ctk.CTkLabel(master= self.frame, text= "Fornecedor cadastrado com sucesso")
                label_sucesso.place(x= 107.5, y= 220)
                
                
            except Exception as e:
                print("Erro ao cadastrar produto, Erro: {e}")
            
            mycursor.close() 
                    
    def frame_listarFornedores(self):
        frame2 = ctk.CTkFrame(master= self.janela, width= 335, height= 380, fg_color= "black").place(x= 355, y= 10)
        self.listarFornecedor()
        
        
    def listarFornecedor(self):
        mycursor = condb.cursor()
        sql = "SELECT Nome, Contato, Endereco FROM fornecedores;"
        mycursor.execute(sql)
        fornecedores = mycursor.fetchall()
        pos_y = 50
        
        for forn in fornecedores:
            label_fornecedores = ctk.CTkLabel(master= self.janela, text= "LISTANDO FORNECEDORES",bg_color= "black", width= 45)
            label_fornecedores.place(x= 450, y= 10)
            label_nome = ctk.CTkLabel(master= self.janela, text= f"Nome: {forn[0]}", bg_color= "black", width= 20)
            label_nome.place(x= 375, y= pos_y)
            pos_y += 30


    def cadastrarCliente(self):
        nome = self.entry_nomeCli.get()
        sobrenome = self.entry_sobrenomeCli.get()
        endereco = self.entry_enderecoCli.get()
        cidade = self.entry_cidadeCli.get()
        codidoPostal = self.entry_CodigoPostalCli.get()
        
        mycursor = condb.cursor()
        sql = 'INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s);'
        valores = (nome, sobrenome, endereco, cidade, codidoPostal)

        try:
            if nome == "" or sobrenome == "" or endereco == "" or cidade == "" or codidoPostal == "":
                label_inserir = ctk.CTkLabel(master= self.frameCliente, text= "* Todas as informações são de caracter obrigatório")
                label_inserir.place(x= 61, y= 350)
                self.janela_cadastro.after(5000, label_inserir.destroy)
                
            else: 
                mycursor.execute(sql, valores)
                condb.commit()
                self.entry_nomeCli.delete(0, 'end')
                self.entry_sobrenomeCli.delete(0, 'end')
                self.entry_enderecoCli.delete(0, 'end')
                self.entry_cidadeCli.delete(0, 'end')
                self.entry_CodigoPostalCli.delete(0, 'end')
                label_sucesso = ctk.CTkLabel(master= self.frameCliente, text= "Cliente cadastrado com sucesso!").place(x= 123.6, y= 350)
                
        except Exception as e:
            print(f"Erro: {e}")
            
        except Error as e:
            
            condb.rollback()
            print(f"Erro: {e}")
        
        finally:
            mycursor.close()
            
main = Aplicacao()    