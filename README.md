# Projeto Aplicado I - Olist

**Autor:** Henrique Fernandes Corradini - RA 1077304  
**Curso:** Tecnologia em Banco de Dados  
**Recorte:** etapas 1 e 2.

**Entrega atual (05/10):** documento inicial complementado com proposta analítica e análise exploratória; scripts Python e notebook executado. Produtos das etapas 3 e 4 não integram esta entrega.

## Sumário
1. [Objetivo](#objetivo)
2. [Organização](#organização)
3. [Reprodução](#reprodução)
4. [Dados e licença](#dados-e-licença)
5. [Métodos e limites](#métodos-e-limites)

## Objetivo
Investigar a associação entre prazo, atraso de entrega, frete e avaliação dos clientes da Olist, usando a base pública histórica de pedidos disponibilizada pela empresa no Kaggle. Não avaliar a operação atual nem inferir causalidade.

## Organização
- `Analise_Exploratoria_Olist.ipynb`: notebook Python com código, documentação e saídas da análise.
- `acquire.py`: aquisição da base oficial e das fontes, com manifesto e hashes.
- `analyze.py`: análise, gráficos e verificação executável mínima.
- `analysis/`: resultados tabulares, indicadores e figuras.
- `sources/`: metadados e registro das fontes consultadas.
- `data/`: dados originais, ignorados pelo Git; obtidos por `acquire.py`.
- `relatorio/`: relatório das etapas 1 e 2 em PDF.

O relatório final encontra-se em `relatorio/Projeto_Aplicado_I_Olist_Etapas_1_e_2.pdf`.

## Reprodução
Com Python 3.12 ou posterior, em um ambiente virtual, instale `requirements.txt`, execute `python acquire.py` e `python analyze.py`.

O notebook também executa a análise integral. Abra-o com a pasta atual apontando para este repositório. Não exige credenciais do Kaggle para o endpoint público usado na aquisição. A disponibilidade do endpoint pode mudar; uma falha de acesso deve ser reportada, nunca substituída por dados inventados.

`python -c "from analyze import self_check; print(self_check())"` verifica agregações com múltiplos itens e pagamentos, escolha da avaliação mais recente, ausência de data e entrega no dia previsto. A análise verifica ainda cardinalidade das junções e reconciliação dos totais.

## Dados e licença
Fonte: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  
Licença informada pela fonte: CC BY-NC-SA 4.0. Atribuição à Olist, uso não comercial e compartilhamento de adaptações dos dados sob a mesma licença. O uso educacional não autoriza reidentificação de pessoas.

Arquivo oficial adquirido em 05/10/2026, versão 2, atualização informada pela API em 01/10/2021. As datas de compra observadas vão de 04/09/2016 a 17/10/2018. Identificadores, localização e textos livres não são publicados no relatório; apresentam-se agregados.

## Métodos e limites
Uma linha por pedido; agregação independente de itens e pagamentos antes das junções; avaliação mais recente por pedido, com desempate por data de criação e identificador. Atraso é a diferença entre datas de calendário; a data estimada inclui todo o dia. Ausências não são imputadas e outliers não são automaticamente removidos.

São calculadas estatísticas descritivas, Pearson para medidas quantitativas e Spearman para notas ordinais. A moeda não está explícita nos arquivos e metadados acessados: os resultados usam UM, unidade monetária original do CSV. Valores de pedidos não são receita líquida, lucro ou faturamento da Olist.
