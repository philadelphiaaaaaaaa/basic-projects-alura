'''
Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

    Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

    >>>> "A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"

'''

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]
# utilizar a função zip(first_list, second_list), agrupa elementos de duas ou mais listas em sequência

def calculating_points(gols_marcados, gols_sofridos):
  vitorias = 0
  derrotas = 0
  empates = 0
  qtd_partidas_jogadas = len(gols_marcados)

  for gols_marcados, gols_sofridos in zip(gols_marcados, gols_sofridos):
    if gols_marcados > gols_sofridos:
      print('Vitória')
      vitorias += 3
    elif gols_marcados < gols_sofridos:
      print('Derrota')
      derrotas += 0
    elif gols_marcados == gols_sofridos:
      print('Empate')
      empates += 1
  
  total_pts = vitorias + empates
  aproveitamento = (total_pts / (qtd_partidas_jogadas * 3)) * 100
  
  return print(f'Pontos Totais: {total_pts}\nAproveitamento: {round(aproveitamento, 1)}%')

    
calculating_points(gols_marcados, gols_sofridos)