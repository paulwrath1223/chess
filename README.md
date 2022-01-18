# chess

## Chess notation
- Chess notation combines the chess piece moved with the new square it has moved to, on the chessboard.
- Chess notation uses abbreviations for each piece, using capitalized letters.
- King = K, Queen = Q, Bishop = B, Knight = N, Rook = R, Pawn = no notation.
- Capturing an enemy piece sees an “x” placed between the piece moved and the square the captured piece was upon.
- When the opponent’s king is threatened by check, a “+” sign is added to the end of the notation.
- Castling kingside is written as “0-0”. Castling queenside is notated with “0-0-0”



## Disambiguating moves
- https://en.wikipedia.org/wiki/Algebraic_notation_(chess)

When two (or more) identical pieces can move to the same square, the moving piece is uniquely identified by specifying the piece's letter, followed by (in descending order of preference):

the file of departure (if they differ); or
the rank of departure (if the files are the same but the ranks differ); or
both the file and rank of departure (if neither alone is sufficient to identify the piece – which occurs only in rare cases where a player has three or more identical pieces able to reach the same square, as a result of one or more pawns having promoted).
In the diagram, both black rooks could legally move to f8, so the move of the d8-rook to f8 is disambiguated as Rdf8. For the white rooks on the a-file which could both move to a3, it is necessary to provide the rank of the moving piece, i.e., R1a3.

In the case of the white queen on h4 moving to e1, neither the rank nor file alone are sufficient to disambiguate from the other white queens. As such, this move is written Qh4e1.

As above, an "x" can be inserted to indicate a capture; for example, if the final case were a capture, it would be written as Qh4xe1.

## Sample Datapoint
 - goal is to be able to import and export in such a format:
 - "17 1999.11.20 1-0 2851 None 51 date_false result_false welo_false belo_true edate_false setup_false fen_false result2_false oyrange_false blen_false ### W1.e4 B1.c6 W2.d4 B2.d5 W3.exd5 B3.cxd5 W4.Bd3 B4.Nc6 W5.c3 B5.Nf6 W6.Bf4 B6.Bg4 W7.Qb3 B7.Qd7 W8.Nd2 B8.e6 W9.Ngf3 B9.Bd6 W10.Ne5 B10.Bxe5 W11.dxe5 B11.Nh5 W12.Be3 B12.a6 W13.h3 B13.Nxe5 W14.Bf1 B14.Bf5 W15.g4 B15.Nd3+ W16.Bxd3 B16.Bxd3 W17.gxh5 B17.Rc8 W18.Rg1 B18.f6 W19.h6 B19.g6 W20.O-O-O B20.d4 W21.Bxd4 B21.Ke7 W22.Nf3 B22.e5 W23.Rxd3 B23.exd4 W24.Re1+ B24.Kf8 W25.Rxd4 B25.Qc6 W26.Qb4+ "