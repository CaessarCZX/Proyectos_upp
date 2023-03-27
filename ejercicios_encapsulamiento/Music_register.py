'''
Vmos a crear una clase llamada registro musical en la cual tendremos como atributos
>>>> nombre de la cancion(verificacion), genero(sin verificacion) y artista(verficacion)
'''

import re

class Musical_register():
    def __init__(self, song_name = 'unknowed-song', gender = 'none', artist ='unknow-artist'):
        self.__song_name = song_name
        self.__gender = gender
        self.__artist = artist

    @property
    def song_name(self):
        return self.__song_name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def artist(self):
        return self.__artist
    
    #Esta funcion solo verifica que el nombre que se le va a poner a la cancion sea solo con letras y no numeros
    @song_name.setter
    def song_name(self, new_name):
        if re.match('^[a-zA-Z]+$',new_name):
            self.__song_name = new_name
            print('Nombre aceptado')
        else:
            print('Nombre no valido')
    
    @gender.setter
    def gender(self,new_gender):
        self.__gender = new_gender

    #Esta funcion solo verifica que el nombre del artista no sea tan corto
    @artist.setter
    def artist(self, new_artist):
        min_len = 3

        if len(new_artist) < min_len:
            print('Nombre no valido')
        else:
            self.__artist = new_artist
            print('Nombre cambiado con exito')

    def song_register(self):
        return f'Name song: {self.song_name}, Gender: {self.gender}, Artist: {self.artist}'

if __name__ == '__main__':
    music_reg_01 = Musical_register()
    music_reg_01.song_name = 'Yellow'
    music_reg_01.gender = 'Pop'
    music_reg_01.artist = 'Coldplay'
    print(music_reg_01.song_register())
