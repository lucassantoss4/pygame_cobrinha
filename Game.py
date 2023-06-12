# pygame_cobrinha
#Repositório do game

import pygame
from pygame.locals import *
from sys import exit 
from random import randint # sorteia valores em um determinado intervalo 


# inicia o jogo
pygame.init()
  
import pygame
 
pygame.init()
 
white = (00, 000, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
X = 594
Y = 480
 
display_surface = pygame.display.set_mode((X, Y))
 
pygame.display.set_caption('Show Text')
 
font = pygame.font.Font('freesansbold.ttf', 32)
 
text = font.render('EPICGAME.cobrinha', True, green, blue)
 
textRect = text.get_rect()
 
textRect.center = (X // 2, Y // 2)
 

 
    
    
display_surface.fill(white)
 
    
    
    
display_surface.blit(text, textRect)
 
    
    
for event in pygame.event.get():
 
      
      if event.type == pygame.QUIT:
 
              pygame.quit()
 
              quit()
 
      pygame.display.update()
    

# Variable to keep our game loop running
running = True
  
# game loop
while running:
    fonti= pygame.font.SysFont('arial',20, True, True)
    men2 = 'bem vindo!'
    txt = fonti.render(men2, True, (000, 255, 255))
    retu = txt.get_rect()

# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
#criar musica de fundo
pygame.mixer.music.set_volume(0.15) # alterar o volume do fundo 
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1 ) # tocar musica de fundo

# barulho da colisao
barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.3) # volume da colisao

#Descrição da tela
largura = 594
altura = 480

# Variaveis display 
x_cobra = int(largura/2) # posicao do retangulo
y_cobra = int(altura/2)

velocidade = 10
x_controle =velocidade
y_controle = 0


# Intervalo de tempo do retangulo azul com a função randint
x_maca = randint (40, 594) # posição em X
y_maca = randint (50, 430) # posição Y

# contador de pontos
pontos = 0
# texto: (parametro(arial), tamanho, negrito(True ou False), italico(True ou False))
fonte =pygame.font.SysFont('arial', 40, bold=True, italic=True)
# pygame.font.get_fonts() comando para ver as fontes disponiveis

tela_game = pygame.display.set_mode((largura, altura))
fundo = pygame.image.load('cobra.png').convert()
tela_game.blit(fundo, (0,0))

# nome do jogo
pygame.display.set_caption('Jogo da cobrinha')



#ranking
colocacao = 0

# taxa de frems do retangulo 
relogio = pygame.time.Clock()

lista_cobra = []

# Limites para o tamanho 
comprimento_inicial = 9

#caso a cobra encoste nela mesma 
morreu = False
# função que desenha o corpo da cobra 
def aumenta_cobra (lista_cobra):
    for XeY in lista_cobra : # XeY = [X,Y]
        pygame.draw.rect(tela_game, (0 , 255, 0), (XeY[0], XeY [1], 20 , 20))

# reiniciar jogo
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0 
    comprimento_inicial = 5
    x_cobra = int(largura/2) 
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint (40, 594)
    y_maca = randint (50, 430) 
    morreu= False 



# lupi do jogo
while True:
    
    novo_jogador = 0
    if pontos <=50:
         relogio.tick(25)
    if pontos <= 100:
        relogio.tick(35)
    if pontos <= 500:
        relogio.tick(45)
        # quanto maior o numero de frems mais rapido o retangulo vaiu rodar
    tela_game.fill((255,255,255)) #preenche com a cor da tela
    mensagem = 'Pontos:{0} Recorde:{1}'.format(pontos, colocacao) # o que vai aparecer  na tela game
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame .quit()
            exit ()


        # condicao 
        # cobra altomatica
        if event.type == KEYDOWN:
            if event.key == K_LEFT :
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    tela_game.fill((0,0,0))
    tela_game.blit(fundo,(0,0))

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle



    # desenha retangulo: ((parametro),(cor do retangulo),{(posicao(x,y)),(combrimento(largura em pix))(altura em pix)}
    # pygame.draw.rect(tela_game,(0,255,0),(200,300,40,50)) # (200,300,40,50) é {(posicao(x,y)),(combrimento(largura em pix))(altura em pix)}
    # pygame.display.update() # a cada iteração do jogador , atualiza a tela 
    cobra = pygame.draw.rect(tela_game, (0,255,0), (x_cobra, y_cobra , 20 , 20)) # (200,300,40,50) é {(posicao(x,y)),(combrimento(largura em pix))(altura em pix)}
    maca= pygame.draw.rect(tela_game, (255,0,0), (x_maca, y_maca ,20, 20)) # quadrado azul

# caso o retangulo vermelho (ret_vermelho) encoste no azul COLISÃO
    if cobra.colliderect(maca):
        x_maca = randint (40, 594)
        y_maca = randint (50, 430)
        pontos +=10
        barulho_colisao.play()
        comprimento_inicial +=1
        colocacao += 10
    # novo raking 
    if colocacao < novo_jogador:
        colocacao+= novo_jogador 
        # novo_jogador.append(colocacao)
         # adiciona um no tamanho 
    #  adicionar tamanho para a cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)



#texto quando perde
    if lista_cobra.count (lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial',20, True, True)
        mensagem = 'Game over!, seus pontos foram {0} - R PRA Continuar'.format(pontos)
        texto_formatado = fonte2.render(mensagem, True, (0, 0 , 0))
        ret_texto = texto_formatado.get_rect()
        
    



        # Condiçã0o de perda 
        morreu =  True
        while morreu :
            tela_game.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            

            ret_texto.center = (largura//2 , altura//2)
            tela_game.blit(texto_formatado, (ret_texto))
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    


    if len (lista_cobra) > comprimento_inicial:
        del lista_cobra[0]




    aumenta_cobra (lista_cobra)


    # apresenta o texto na tela (parametro,(posicao(x,y))
    tela_game.blit(texto_formatado,(000,000))
    #print ('colidiu') subistituido por X ,Y
    pygame.display.update()
