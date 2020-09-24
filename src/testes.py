import jogovelha
import sys

erroInicializar = False
jogo = jogovelha.inicializar()

if len(jogo) != 3:
        erroInicializar = True
else:
        for linha in jogo:
<<<<<<< HEAD
                if len(linha) != 3;
                        erroInicializar = True
                else:
                        for elemento in linha:
                                if elemento != ".":
=======
                if len(linha) != 3:
                        erroInicializar = True
                else:
                        for elemento in linha:
                                if elemento != '.':
>>>>>>> v1
                                        erroInicializar = True
if erroInicializar:
        sys.exit(1)
else:
<<<<<<< HEAD
        sys.exit(0)
=======
        sys.exit(0
>>>>>>> v1
