# Projeto Aplicado I - Olist

**Autor:** Henrique Fernandes Corradini - RA 1077304  
**Curso:** Tecnologia em Banco de Dados  
**Recorte:** etapas 1 a 3.

## Objetivo
Investigar como prazo, atraso e frete se associam às avaliações dos clientes da Olist e comunicar os resultados da análise exploratória com uma narrativa orientada por dados. O estudo usa o recorte histórico de 2016 a 2018; não representa a operação atual nem estabelece causalidade.

## Entregas
- `relatorio/Projeto_Aplicado_I_Olist_Etapas_1_a_3.pdf`: documento consolidado, com a definição do projeto, proposta analítica, AED e roteiro de Data Storytelling.
- `relatorio/Projeto_Aplicado_I_Olist_Etapas_1_e_2.pdf`: versão entregue para a etapa 2.
- `Analise_Exploratoria_Olist.ipynb`: notebook Python com código, verificações, resultados e gráficos.
- `acquire.py`: obtenção da base pública oficial e registro de fontes e hashes.
- `analyze.py`: integração, validação, estatísticas e gráficos exploratórios e narrativos.
- `analysis/`: resultados tabulares, indicadores e figuras reproduzíveis.
- `sources/`: metadados do conjunto de dados e registro da aquisição.

## Reprodução
Com Python 3.12 ou posterior, instale as dependências de `requirements.txt` em um ambiente virtual, execute `python acquire.py` e depois `python analyze.py`. O notebook também contém as células executáveis da análise e foi executado com a versão documentada dos dados. O conjunto público é baixado do endpoint oficial do Kaggle; não é necessário incluir os CSVs no repositório.

A checagem mínima cobre pedidos com múltiplos itens e pagamentos, avaliação mais recente, datas ausentes e entrega na data estimada. A execução também verifica chaves, cardinalidade das junções, pedidos órfãos e reconciliação dos totais agregados.

## Dados e limites
Fonte: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), versão 2. Licença informada pela fonte: CC BY-NC-SA 4.0; uso educacional não comercial, com atribuição e respeito às condições de compartilhamento.

Uma linha da análise representa um pedido. Itens e pagamentos são agregados antes das junções; avaliações repetidas são reduzidas à resposta mais recente pela regra documentada no notebook. Ausências não são imputadas e outliers permanecem na análise. A moeda não está explicitamente identificada nos metadados consultados; os valores são indicados como unidade monetária original (UM).

A apresentação narrativa compara taxa de atraso, avaliações baixas e diferenças geográficas. Os denominadores são apresentados junto aos percentuais. Os dados históricos permitem descrever associações e indicar situações para investigação, sem demonstrar causas ou estimar desempenho atual.
