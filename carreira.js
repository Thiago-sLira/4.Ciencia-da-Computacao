const contas = [
  { numero: 12345, saldo: 1000 },
  { numero: 54321, saldo: 500 },
  { numero: 98765, saldo: 2500 }
];

const transferencia1 = { contaOrigem: 12345, contaDestino: 54321, valor: 500 }
const transferencia2 = { contaOrigem: 54321, contaDestino: 12345, valor: 600 }
const transferencia3 = { contaOrigem: 56789, contaDestino: 98765, valor: 200 }
const transferencia4 = { contaOrigem: 98765, contaDestino: 56789, valor: 200 }

// Criar uma função para realizar a transferência de fato recebendo um objeto:
// {
//   contaOrigem, contaDestino, valor
// }
// Criar uma função que busca se a conta
//   Caso a conta não exista, retorne uma mensagem "Conta não existe"
// Verifica se, em uma conta existente, tem saldo suficiente
//   Caso o saldo da conta origem existente não seja suficiente, retornar uma mensagem "Saldo insuficiente"
// Criar uma função para atualizar os valores na DB
// Caso as validações anteriores estejam ok, realizar a transferência e retornar uma mensagem: "Transferência realizada com sucesso"

const verificaSeContaExiste = (numeroDaConta) => {
  return contas.find(({ numero }) => numero === numeroDaConta);
};

const atualizaSaldosNaDB = (dados) => {
  contas.forEach((conta, index) => {
    if (conta.numero === dados.contaOrigem) {
      contas[index].saldo -= dados.valor;
      console.log("Conta encontrada");
    }

    if (conta.numero === dados.contaDestino) {
      contas[index].saldo += dados.valor;
      console.log("Conta encontrada");
    }
  });
};

const transferir = (dados) => {
  const contaOrigem = verificaSeContaExiste(dados.contaOrigem);
  const contaDestino = verificaSeContaExiste(dados.contaDestino);

  if (!contaOrigem || !contaDestino) {
    return "Conta não existe"
  }

  if (contaOrigem.saldo < dados.valor) {
    return "Saldo insuficiente"
  }

  atualizaSaldosNaDB(dados);

  return "Transferência realizada com sucesso"
};

console.log(transferir(transferencia1));
console.log(contas);
