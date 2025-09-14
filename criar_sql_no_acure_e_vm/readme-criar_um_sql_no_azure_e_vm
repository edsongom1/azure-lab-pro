# 🚀 Configuração de Banco de Dados SQL no Microsoft Azure

## 📋 Descrição do Projeto

Este repositório documenta o processo prático de configuração de uma instância de Banco de Dados SQL na plataforma Microsoft Azure, desenvolvido como parte do desafio de aprendizagem da DIO (Digital Innovation One).

## 🎯 Objetivos

- Aplicar conceitos de cloud computing na prática
- Configurar e provisionar recursos de banco de dados na Azure
- Documentar processos técnicos de forma estruturada
- Demonstrar conhecimentos em administração de bancos de dados na nuvem

## 🛠️ Recursos Utilizados

- **Microsoft Azure Portal**
- **Azure SQL Database**
- **Máquinas Virtuais do Azure**
- **Resource Groups (Grupos de Recursos)**

## 📖 Passo a Passo da Configuração

### 1. Acesso ao Portal Azure

- Acesse o portal: `https://portal.azure.com`
- Navegue até "Bancos de dados SQL" no menu lateral

### 2. Criação do Banco de Dados SQL

#### Configurações Básicas:
- **Nome do banco de dados**: `testeteste`
- **Servidor**: Criação de novo servidor SQL
- **Nome do servidor**: `testestes.database.windows.net`
- **Localização**: `(US) East US`
- **Ambiente**: Desenvolvimento
- **Pool elástico SQL**: Não utilizado

#### Configurações de Computação e Armazenamento:
- **Camada de serviço**: Uso Geral - Sem servidor
- **Configuração**: Série Standard (Gen5), 1 vCore, 32 GB de armazenamento
- **Zona redundante**: Desabilitada
- **Redundância de backup**: Armazenamento de backup com redundância geográfica

### 3. Configuração de Máquina Virtual (Opcional)

Para casos que necessitem de VM para aplicações:

#### Detalhes da Instância:
- **Região**: `(US) East US`
- **Zona de disponibilidade**: Zonas 1
- **Tipo de segurança**: Computadores virtuais de inicialização confiável
- **Imagem**: Windows Server 2019 Datacenter - x64 Gen2
- **Arquitetura**: x64
- **Tamanho**: Standard_DS1_v2 - 1 vcpu, 3.5 GiB memória

#### Configurações de Disco:
- **Tamanho do disco do SO**: Padrão de imagem (127 GiB)
- **Tipo de disco do SO**: SSD Premium (armazenamento com redundância local)
- **Excluir com VM**: Habilitado

#### Monitoramento:
- **Diagnóstico de inicialização**: Habilitado com conta de armazenamento gerenciada
- **Alertas**: Configuração opcional de regras de alerta recomendadas
- **Integridade**: Monitoramento de integridade do aplicativo disponível

## 💰 Estimativa de Custos

### Banco de Dados SQL:
- **Uso Geral (GP_S_Gen5_1)**
- **Custo por GB**: R$ 0,63 (em BRL)
- **Armazenamento máximo selecionado**: 41.6 GB
- **Custo estimado de armazenamento/mês**: R$ 26,25
- **Custo de cálculo/vCore segundo**: R$ 0,000795

### Observações Importantes:
- Os bancos de dados sem servidor são cobrados por segundo de vCore com base em uma combinação de uso de CPU e memória
- Configurações padrão fornecidas para cargas de trabalho de desenvolvimento
- As configurações podem ser modificadas conforme necessário

## 🔧 Configurações de Segurança

- **Autenticação**: Microsoft Entra ID (anteriormente Azure AD)
- **Métodos de autenticação recomendados**:
  - SQL e Microsoft Entra para administração
  - Apenas autenticação do Microsoft Entra para aplicações
- **Firewall**: Configuração necessária para acesso externo

## 📊 Monitoramento e Manutenção

### Recursos de Monitoramento Disponíveis:
- Diagnósticos de inicialização
- Alertas de performance
- Monitoramento de integridade do aplicativo
- Métricas de uso de recursos

### Backup e Recuperação:
- **Redundância de armazenamento de backup**: Geográfica
- **Replicação**: Backups PITR e LTR replicados geograficamente
- **Recuperação**: Capacidade de recuperação de interrupção regional disponível

## 🎓 Conhecimentos Adquiridos

- **Provisionamento de recursos na Azure**
- **Configuração de bancos de dados SQL na nuvem**
- **Gerenciamento de custos e otimização**
- **Implementação de práticas de segurança**
- **Monitoramento e manutenção de recursos**
- **Compreensão de SLA e disponibilidade**

## 🔗 Recursos Úteis

- [Documentação oficial do Azure SQL Database](https://docs.microsoft.com/azure/sql-database/)
- [Melhores práticas de segurança](https://docs.microsoft.com/azure/sql-database/sql-database-security-best-practice)
- [Guia de preços do Azure SQL](https://azure.microsoft.com/pricing/details/sql-database/)

## 👨‍💻 Autor

Desenvolvido como parte do bootcamp da DIO - Digital Innovation One

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**💡 Dica**: Este documento serve como referência para futuras implementações e pode ser adaptado conforme necessidades específicas do projeto.