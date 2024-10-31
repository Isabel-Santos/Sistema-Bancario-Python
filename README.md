# Sistema Bancário

Este projeto é um sistema bancário simples desenvolvido em Python, que permite realizar operações básicas como depósito, saque e extrato. O objetivo é gerenciar as finanças de forma prática e intuitiva. Como versão otimizada, também inclui funcionalidades para cadastrar usuários e contas bancárias.

## Funcionalidades

- **Cadastro de Clientes**: Permite o registro de clientes no sistema, incluindo dados pessoais.
- **Gerenciamento de Contas**: Os clientes podem ter múltiplas contas, e o sistema suporta operações como depósitos e saques.
- **Registro de Transações**: Todas as transações são registradas, permitindo a consulta do histórico de operações.
- **Limites de Saque**: Contas correntes podem ter limites de saque definidos.

## Estrutura do Código

O sistema é dividido em várias classes:

- **Cliente**: Classe base para os clientes do banco.
- **PessoaFisica**: Classe derivada que representa clientes pessoas físicas.
- **Conta**: Classe base para diferentes tipos de contas.
- **ContaCorrente**: Classe derivada que implementa contas correntes.
- **Transacao**: Classe abstrata para representar transações financeiras.
- **Saque**: Classe que representa a operação de saque.
- **Deposito**: Classe que representa a operação de depósito.
- **Historico**: Classe que armazena o histórico de transações.

## Requisitos

- Python 3.x