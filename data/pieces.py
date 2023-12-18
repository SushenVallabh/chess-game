import pygame

white_pawn = pygame.image.load("data/white_pawn.png")
white_pawn = pygame.transform.scale(white_pawn, (100, 100))
black_pawn = pygame.image.load("data/black_pawn.png")
black_pawn = pygame.transform.scale(black_pawn, (100, 100))
white_king = pygame.image.load("data/white_king.png")
white_king = pygame.transform.scale(white_king, (100, 100))
black_king = pygame.image.load("data/black_king.png")
black_king = pygame.transform.scale(black_king, (100, 100))
white_bishop = pygame.image.load("data/white_bishop.png")
white_bishop = pygame.transform.scale(white_bishop, (100, 100))
black_bishop = pygame.image.load("data/black_bishop.png")
black_bishop = pygame.transform.scale(black_bishop, (100, 100))
white_rook = pygame.image.load("data/white_rook.png")
white_rook = pygame.transform.scale(white_rook, (100, 100))
black_rook = pygame.image.load("data/black_rook.png")
black_rook = pygame.transform.scale(black_rook, (100, 100))
white_queen = pygame.image.load("data/white_queen.png")
white_queen = pygame.transform.scale(white_queen, (100, 100))
black_queen = pygame.image.load("data/black_queen.png")
black_queen = pygame.transform.scale(black_queen, (100, 100))
white_knight = pygame.image.load("data/white_knight.png")
white_knight = pygame.transform.scale(white_knight, (100, 100))
black_knight = pygame.image.load("data/black_knight.png")
black_knight = pygame.transform.scale(black_knight, (100, 100))
red = pygame.image.load("data/red.jpg")
red = pygame.transform.scale(red, (100, 100))
blue = pygame.image.load("data/blue.png")
blue = pygame.transform.scale(blue, (100, 100))


all_pieces = {'white_pawn': white_pawn, 'black_pawn': black_pawn, 'white_king': white_king, 'black_king': black_king,
              'white_queen': white_queen, 'black_queen': black_queen, 'white_rook': white_rook, 'black_rook': black_rook,
              'white_bishop': white_bishop, 'black_bishop': black_bishop, 'white_knight': white_knight, 'black_knight': black_knight}
