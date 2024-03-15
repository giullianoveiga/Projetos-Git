from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


# Classes e métodos do sistema de gerenciamento de estoque
class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def atualizar_estoque(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)
        if produto:
            produto.quantidade += quantidade
            print(f"Estoque atualizado para o produto {produto.nome}. Nova quantidade: {produto.quantidade}")
        else:
            print("Produto não encontrado.")


# Exemplo de uso das classes
estoque = Estoque()

produto1 = Produto("001", "Camisa", 29.99, 50)
produto2 = Produto("002", "Calça", 49.99, 30)

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)

cliente1 = Cliente("João", "Rua A, 123")
pedido1 = Pedido(cliente1)
pedido1.adicionar_item(produto1, 2)
pedido1.adicionar_item(produto2, 1)

print("Pedido do cliente", pedido1.cliente.nome)
for item in pedido1.itens:
    print(item["produto"].nome, "-", item["quantidade"])

estoque.atualizar_estoque("001", -2)
estoque.atualizar_estoque("002", -1)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/novo_pedido', methods=['POST'])
def novo_pedido():
    cliente_nome = request.form['cliente_nome']
    produto_codigo = request.form['produto_codigo']
    quantidade = int(request.form['quantidade'])
    # Lógica para processar o novo pedido
    return redirect(url_for('index'))  # Redireciona de volta para a página inicial após o processamento


@app.route('/atualizar_estoque', methods=['POST'])
def atualizar_estoque():
    codigo_produto = request.form['codigo_produto']
    quantidade_atualizar = int(request.form['quantidade_atualizar'])
    estoque.atualizar_estoque(codigo_produto, quantidade_atualizar)  # Chama o método para atualizar o estoque
    return redirect(url_for('index'))  # Redireciona de volta para a página inicial após o processamento


@app.route('/estoque_atualizado')
def estoque_atualizado():
    return jsonify(estoque=[produto.__dict__ for produto in estoque.produtos])


@app.route('/adicionar_produto', methods=['POST'])
def adicionar_produto():
    novo_produto_codigo = request.form['novo_produto_codigo']
    novo_produto_nome = request.form['novo_produto_nome']
    novo_produto_quantidade = int(request.form['novo_produto_quantidade'])

    novo_produto = Produto(novo_produto_codigo, novo_produto_nome, 0, novo_produto_quantidade)
    estoque.adicionar_produto(novo_produto)

    return redirect(url_for('index'))  # Redireciona de volta para a página inicial após o processamento


if __name__ == '__main__':
    app.run(debug=True)
