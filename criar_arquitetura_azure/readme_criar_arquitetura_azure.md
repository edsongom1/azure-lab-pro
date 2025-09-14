# Desafio Azure: Criação de Recursos na Nuvem

## 📋 Descrição do Projeto

Este projeto demonstra o processo prático de criação e configuração de recursos no Microsoft Azure, incluindo grupos de recursos e redes virtuais. O objetivo é documentar o passo a passo realizado através do portal Azure, servindo como referência para futuras implementações.

## 🎯 Objetivos

- Criar um grupo de recursos no Azure
- Configurar uma rede virtual (VNet)
- Aplicar boas práticas de organização de recursos
- Documentar o processo completo com screenshots

## 🛠️ Recursos Criados

### 1. Grupo de Recursos
- **Nome:** AZ-900_Lab_DIO
- **Assinatura:** Assinatura de Plataformas MSDN
- **Região:** East US 2
- **Status:** Criado com sucesso

### 2. Rede Virtual
- **Nome:** VNET1
- **Grupo de Recursos:** AZ-900_Lab_DIO
- **Região:** Brazil South
- **Espaço de Endereço:** 10.0.0.0/16 (65.536 endereços)
- **Configurações de Segurança:**
  - Azure Bastion: Desabilitado
  - Firewall do Azure: Desabilitado
  - Proteção de Rede do DDoS: Desabilitado

## 📸 Documentação Visual

O projeto inclui uma série de screenshots organizados na pasta `/images` que documentam:

1. **Criação do Grupo de Recursos:**
   - Configuração inicial (Básico)
   - Aplicação de marcações (Tags)
   - Validação e revisão
   - Confirmação de criação

2. **Configuração da Rede Virtual:**
   - Seleção do grupo de recursos
   - Configuração de endereçamento IP
   - Definições de segurança
   - Deployment bem-sucedido

3. **Verificação dos Recursos:**
   - Visualização do grupo de recursos criado
   - Status dos recursos implantados
   - Controle de acesso (IAM)
   - Visualizador de recursos

## 🔧 Passo a Passo Executado

### Etapa 1: Criação do Grupo de Recursos
1. Acessar o portal Azure (portal.azure.com)
2. Navegar para "Grupos de recursos"
3. Clicar em "Criar"
4. Preencher os dados básicos:
   - Assinatura: Assinatura de Plataformas MSDN
   - Nome do grupo: AZ-900_Lab_DIO
   - Região: East US 2
5. Aplicar marcações (se necessário)
6. Revisar e criar

### Etapa 2: Criação da Rede Virtual
1. Acessar "Redes virtuais" no portal
2. Clicar em "Criar rede virtual"
3. Configurar detalhes básicos:
   - Grupo de recursos: AZ-900_Lab_DIO
   - Nome: VNET1
   - Região: Brazil South
4. Configurar endereços IP (10.0.0.0/16)
5. Manter configurações de segurança padrão
6. Revisar e criar

### Etapa 3: Verificação e Validação
1. Confirmar criação dos recursos
2. Verificar status no grupo de recursos
3. Validar configurações da rede virtual
4. Testar acesso via portal

## 📚 Conceitos Aplicados

- **Grupos de Recursos:** Organização lógica de recursos relacionados
- **Redes Virtuais:** Isolamento de rede na nuvem Azure
- **Regiões Azure:** Distribuição geográfica dos recursos
- **Gerenciamento de Identidade:** Controle de acesso (IAM)
- **Marcações (Tags):** Organização e controle de custos

## 🔗 Links Úteis

- [Documentação Oficial do Azure](https://docs.microsoft.com/azure/)
- [Portal Azure](https://portal.azure.com)
- [Azure Resource Groups](https://docs.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal)
- [Virtual Networks](https://docs.microsoft.com/azure/virtual-network/)
- [DIO - Digital Innovation One](https://dio.me/)

## 🚀 Próximos Passos

- [ ] Criar máquinas virtuais na rede configurada
- [ ] Implementar grupos de segurança de rede (NSGs)
- [ ] Configurar monitoramento com Azure Monitor
- [ ] Explorar serviços de armazenamento
- [ ] Implementar soluções de backup

## 🤝 Contribuindo

Este é um projeto de aprendizado da DIO. Sinta-se à vontade para:
- Fazer fork do repositório
- Sugerir melhorias
- Compartilhar sua experiência
- Reportar issues

## 📝 Notas

- Todos os recursos foram criados em ambiente de laboratório
- Lembre-se de monitorar os custos dos recursos criados
- Sempre revise as configurações de segurança antes da produção
- Este projeto faz parte do bootcamp da DIO

## 👨‍💻 Autor

Projeto desenvolvido como parte do desafio prático da Digital Innovation One (DIO).

---

⭐ **Deixe uma estrela se este projeto foi útil para você!**