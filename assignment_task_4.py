# """
# CHESSBOARD
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# """

# # Assignment: finish your chessboard
# white = '\u25A0'         #\u = unicode
# black = '\u25A1'
# white_pawn = '\u2659' # print for outer value 1
# black_pawn = '\u265F' # print for outer value 6

# for outer in range(0,8):
#     for inner in range(0,8):
        
#         if outer == 1:
#             print(white_pawn, end=' ')
#         elif outer == 6:
#             print(black_pawn, end=' ')
#         elif (outer+inner)%2 == 0:
#             print(white, end=' ')
#         else:
#             print(black, end=' ')
        
#     print()

# # —————————————————————————— 


# Chess Board using Unicode

white = '\u25A0'      # ■
black = '\u25A1'      # □

# White Pieces
white_rook   = '\u2656'   # ♖
white_knight = '\u2658'   # ♘
white_bishop = '\u2657'   # ♗
white_queen  = '\u2655'   # ♕
white_king   = '\u2654'   # ♔
white_pawn   = '\u2659'   # ♙

# Black Pieces
black_rook   = '\u265C'   # ♜
black_knight = '\u265E'   # ♞
black_bishop = '\u265D'   # ♝
black_queen  = '\u265B'   # ♛
black_king   = '\u265A'   # ♚
black_pawn   = '\u265F'   # ♟

for row in range(8):

    # Black major pieces
    if row == 0:
        print(
            black_rook,
            black_knight,
            black_bishop,
            black_queen,
            black_king,
            black_bishop,
            black_knight,
            black_rook
        )

    # Black pawns
    elif row == 1:
        for col in range(8):
            print(black_pawn, end=" ")
        print()

    # White pawns
    elif row == 6:
        for col in range(8):
            print(white_pawn, end=" ")
        print()

    # White major pieces
    elif row == 7:
        print(
            white_rook,
            white_knight,
            white_bishop,
            white_queen,
            white_king,
            white_bishop,
            white_knight,
            white_rook
        )

    # Empty squares
    else:
        for col in range(8):
            if (row + col) % 2 == 0:
                print(white, end=" ")
            else:
                print(black, end=" ")
        print()


# #or and more This version is shorter, cleaner, and easier to understand


# —————————————————————————— 

# # Chessboard with all pieces

# white = '\u25A0'      # ■
# black = '\u25A1'      # □

# # White Pieces
# white_rook = '\u2656'      # ♖
# white_knight = '\u2658'    # ♘
# white_bishop = '\u2657'    # ♗
# white_queen = '\u2655'     # ♕
# white_king = '\u2654'      # ♔
# white_pawn = '\u2659'      # ♙

# # Black Pieces
# black_rook = '\u265C'      # ♜
# black_knight = '\u265E'    # ♞
# black_bishop = '\u265D'    # ♝
# black_queen = '\u265B'     # ♛
# black_king = '\u265A'      # ♚
# black_pawn = '\u265F'      # ♟

# # Lists of major pieces
# black_pieces = [
#     black_rook, black_knight, black_bishop, black_queen,
#     black_king, black_bishop, black_knight, black_rook
# ]

# white_pieces = [
#     white_rook, white_knight, white_bishop, white_queen,
#     white_king, white_bishop, white_knight, white_rook
# ]

# # Print Chessboard
# for row in range(8):

#     if row == 0:
#         for piece in black_pieces:
#             print(piece, end=" ")

#     elif row == 1:
#         for col in range(8):
#             print(black_pawn, end=" ")

#     elif row == 6:
#         for col in range(8):
#             print(white_pawn, end=" ")

#     elif row == 7:
#         for piece in white_pieces:
#             print(piece, end=" ")

#     else:
#         for col in range(8):
#             if (row + col) % 2 == 0:
#                 print(white, end=" ")
#             else:
#                 print(black, end=" ")

#     print()






# —————————————————————————— 

# # white = '\u25A0'
# # black = '\u25A1'
# # white_pawn='\u2659'
# # black_pawn='\u265F'
# # for index in range(8):
# #     for index1 in range(8):
# #         if(index==1):
# #             print(white_pawn, end=' ')
# #         elif(index==6):
# #             print(black_pawn, end=' ')
# #         elif((index1+index)%2==0):
# #             print(white, end=' ')
# #         else:
# #             print(black, end=' ')
# #     print()
    