# Projeto: O que vende um carro?

Você é analista na Lista de Eixo de Manivela. Centenas de propagandas gratuitas de veículos são publicadas no seu site todos os dias. Você precisa estudar os dados coletados nos últimos anos e determinar quais fatores influenciaram o preço de um veículo.

Temos os seguintes parâmetros:
- Price
- Age of the vehicle when the advertisement was placed
- Mileage
- Number of cylinders
- Condition

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

**Conclusion**

Vemos uma relação clara entre quanto mais novo o carro, maior o preço e mais caro ele é com menos quilômetros rodados. Os carros automáticos também são claramente mais caros. As cores mais caras são preto, cinza, vermelho e branco. Branco sendo o mais comum (analisado anteriormente com .describe()). Então o carro mais caro seria um carro branco, com baixa quilometragem, novo e automático.

# **Link do aplicativo**
- https://vehicles-us-1-o1f4.onrender.com/
