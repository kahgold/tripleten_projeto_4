# Projeto: O que vende um carro?

Você é analista na Lista de Eixo de Manivela. Centenas de propagandas gratuitas de veículos são publicadas no seu site todos os dias. Você precisa estudar os dados coletados nos últimos anos e determinar quais fatores influenciaram o preço de um veículo.

**Descrição dos dados:**
- O conjunto de dados contém os seguintes campos:
    - `price`
    - `model_year`
    - `model`
    - `condition`
    - `cylinders`
    - `fuel` — gasolina, diesel etc.
    - `odometer` — a quilometragem do veículo quando a propaganda foi publicada
    - `transmission`
    - `paint_color`
    - `is_4wd` — Se o veículo é 4 por 4 (tipo Booleano)
    - `date_posted` — a data que a propaganda foi publicada
    - `days_listed` — dias desde a publicação até a retirada

**Conclusão**

*Mais uma vez realizar esta tarefa foi um grande prazer  e também um desafio, pois este conjunto de dados está bastante “corrompido”, sem dados duplicados mas faltando muitos valores  e  dados em diversas áreas. O formato é diferente do ideal, a parte de processamento de dados e análise exploratória leva um tempo relativamente longo e  em alguns casos requer a criação de correlações e gráficos entre  variáveis ​​para melhor compreender o conjunto de dados. Muitos são valores discrepantes e, ao eliminá-los, perderemos grande parte dos nossos dados.*

*O fator preço é fortemente influenciado pelo odometer e pela idade do veículo, mas é o oposto e  muito significativo. Quanto mais antigo e “usado” for o carro, menor será o preço. O tipo de transmissão que vai dominar o mundo é a transmissão automática, como nos mostra este conjunto de dados. Conveniente, confortável e seguro. O exame das cores dos veículos nos mostra que a ocorrência de cores clássicas continua elevada e mais frequente. Branco, preto, prata, cinza, mas também vermelho e azul. Cores mais “vibrantes” aparecem com menos frequência nos veículos deste conjunto de dados.*

*Enfim, um dataset interessante de se trabalhar onde conseguimos descobrir:*
- os fatores que mais influenciam nos preços dos veículos;
- o tempo médio de dias das propagandas para cada tipo;
- a preferência por transmissão automática;
- que os carros conversíveis tem o menor tempo médio de propaganda ou a venda seja mais rápida;
- que existem pouquíssimos veículos na cor roxa;
- e que mesmo o dataset contendo carros com data de fabricação entre 1908 e 2019, a média e mediana de idade dos veículos ficou entre 2009 e 2011.

# **Link do aplicativo**
- https://vehicles-us-1-o1f4.onrender.com/
