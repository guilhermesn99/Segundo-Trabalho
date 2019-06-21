class Carro:

  consumo=0.0
  distancia=0.0
  combArmazenado=0.0
  addGasolina=0.0
    
  def __init__(self,consumo):
    self.consumo = consumo

  def andar(self,distancia):
    self.combArmazenado = self.combArmazenado - (distancia/self.consumo)

  def obterGasolina(self):
    return (self.combArmazenado)
    
  def adicionarGasolina(self,addGasolina):
    self.combArmazenado = self.combArmazenado + addGasolina

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()

print('O carro gasta 1 Litro de gasolina a cada 15 km.')
print('Adicionando 20 Litros de gasolina e se o carro andar 100 km,') 
print('então o nível de gasolina restante será:')
print(meuFusca.obterGasolina(),'Litros')