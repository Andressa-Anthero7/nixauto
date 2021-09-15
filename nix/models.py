from django.db import models
from django_resized import ResizedImageField
from sorl.thumbnail import ImageField, get_thumbnail


# Create your models here.


class Anuncio(models.Model):
    TIPO = (
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
    )

    MARCAS = (
        ('ACURA','ACURA'),
        ('AGRALE','AGRALE'),
        ('ALFA ROMEO','ALFA ROMEO'),
        ('ASIA MOTOR','ASIA'),
        ('ASTON MARTIN','ASTON'),
        ('AUDI','AUDI'),
        ('BMW','BMW'),
        ('BRANDY','BRANDY'),
        ('CAGIVA','CAGIVA'),
        ('CALOI','CALOI'),
        ('CAOA CHERY','CAOA CHERY'),
        ('CITROEN','CITROEN'),
        ('CHANGAN','CHANGAN'),
        ('CHRYSLER','CHRYSLER'),
        ('CROSS LANDER','CROSS LANDER'),
        ('DAELIM','DAELIM'),
        ('DAEWOO','DAEWOO'),
        ('DAFRA','DAFRA'),
        ('DAIHATSU','DAIHATSU'),
        ('DODGE','DODGE'),
        ('DUCATI','DUCATI'),
        ('EFFA','EFFA'),
        ('ENGESA','ENGESA'),
        ('FERRARI','FERRARI'),
        ('FIAT','FIAT'),
        ('FORD','FORD'),
        ('FOX','FOX'),
        ('FYM','FYM'),
        ('GM-CHEVROLET','GM-CHEVROLET'),
        ('GURGEL','GURGEL'),
        ('HAFEI','HAFEI'),
        ('HARLEY-DAVIDSON','HARLEY-DAVIDSON'),
        ('HARTFORD','HARTFORD'),
        ('HERO','HERO'),
        ('HITECH ELETRIC','HITECH ELETRIC'),
        ('HONDA','HONDA'),
        ('HUSABERG','HUSABERG'),
        ('INDIAN','INDIAN'),
        ('IROS','IROS'),
        ('IVECO','IVECO'),
        ('JAC','JAC'),
        ('JAGUAR','JAGUAR'),
        ('JEEP','JEEP'),
        ('KASINKI','KASINKI'),
        ('KAWAKASI','KAWAKASI'),
        ('KIA MOTORS','KIA MOTORS'),
        ('LADA','LADA'),
        ('LAMBORGHINI','LAMBORGHINI'),
        ('LAND ROVER','LAND ROVER'),
        ('LEXUS','LEXUS'),
        ('LIFAN','LIFAN'),
        ('MAHINDRA','MAHINDRA'),
        ('MALAGUTI','MALAGUTI'),
        ('MATRA','MATRA'),
        ('MAZDA','MAZDA'),
        ('MERCEDEZ-BENZ','MERCEDEZ-BENZ'),
        ('MERCURY','MERCURY'),
        ('MG','MG'),
        ('MINI','MINI'),
        ('MITA','MITA'),
        ('MITSUBISHI','MITSUBISHI'),
        ('MOTOCAR','MOTOCAR'),
        ('MVK','MVK'),
        ('PEGEOUT','PEGEOUT'),
        ('PONTIAC','PONTIAC'),
        ('PORSHE','PORSHE'),
        ('RAM','RAM'),
        ('RENAULT','RENAULT'),
        ('ROLLS-ROYCE','ROLLS-ROYCE'),
        ('SHINERAY','SHINERAY'),
        ('SIAMOTO','SIAMOTO'),
        ('SUNDOWN','SUNDOWN'),
        ('SUZUKI','SUZUKI'),
        ('TAC','TAC'),
        ('TARGOS','TARGOS'),
        ('TIGER','TIGER'),
        ('VOLCANO','VOLCANO'),
        ('YAMAHA','YAMAHA'),
    )

    COMBUSTIVEL = (
            ('GASOLINA','GASOLINA'),
            ('ALCOOL','ALCOOL'),
            ('FLEX','FLEX'),
            ('DIESEL','DIESEL'),
            ('GNV','GNV'),
            ('MIX (ALCOOL/GASOLINA','MIX (ALCOOL/GASOLINA'),
        )

    CAMBIO = (
            ('MANUAL','MANUAL'),
            ('AUTOMÁTICO','AUTOMÁTICO'),
            ('SEMI-AUTOMÁTICO','SEMI-AUTOMÁTICO'),
            
        )

    ANO = (
            ('2021','2021'),
            ('2020','2020'),
            ('2019','2019'),
            ('2018','2018'),
            ('2017','2017'),
            ('2016','2016'),
            ('2015','2015'),
            ('2014','2014'),
            ('2013','2013'),
            ('2012','2012'),
            ('2011','2011'),
            ('2010','2010'),
            ('2009','2009'),
            ('2008','2008'),
            ('2007','2007'),
            ('2006','2006'),
            ('2005','2005'),
            ('2004','2004'),
            ('2003','2003'),
            ('2002','2002'),
            ('2001','2001'),
            ('2000','2000'),
            ('1999','1999'),
            ('1998','1998'),
            ('1997','1997'),
            ('1996','1996'),
            ('1995','1995'),
            ('1994','1994'),
            ('1993','1993'),
            ('1992','1992'),
            ('1991','1991'),
            ('1990','1990'),
            ('1989','1989'),
            ('1988','1988'),
            ('1987','1987'),
            ('1986','1986'),
            ('1985','1985'),
            ('1984','1984'),
            ('1983','1983'),
            ('1982','1982'),
            ('1981','1981'),
            ('1980','1980'),
            ('1979','1979'),
            ('1978','1978'),
            ('1977','1977'),
            ('1976','1976'),
            ('1975','1975'),
            ('1974','1974'),
            ('1973','1973'),
            ('1972','1972'),
            ('1971','1971'),
            ('1970','1970'),
            ('1969','1969'),
            ('1968','1968'),
            ('1967','1967'),
            ('1966','1966'),
            ('1965','1965'),
            ('1964','1964'),
            ('1963','1963'),
            ('1962','1962'),
            ('1961','1961'),
            ('1960','1960'),
            ('1959','1959'),
            ('1957','1957'),
            ('1956','1956'),
            ('1955','1954'),
            ('1953','1953'),
            ('1952','1952'),
            ('1951','1951'),
            ('1950','1950'),
        )
    


    CORES = (
            ('AMARELO','AMARELO'),
            ('AZUL','AZUL'),
            ('BEGE','BEGE'),
            ('BRANCO','BRANCO'),
            ('BRANCO PÉROLA','BRANCO PÉROLA'),
            ('BRONZE','BRONZE'),
            ('CAMUFLADO','CAMUFLADO'),
            ('CHAMPAGNE','CHAMPAGNE'),
            ('CHUMBO','CHUMBO'),
            ('CINZA','CINZA'),
            ('DOURADO','DOURADO'),
            ('GRAFITE','GRAFITE'),
            ('GRENÁ','GRENÁ'),
            ('LARANJA','LARANJA'),
            ('MARRON','MARRON'),
            ('PRATA','PRATA'),
            ('PRETO','PRETO'),
            ('PRETO ONIX','PRETO ONIX'),
            ('ROSA','ROSA'),
            ('ROXO','ROXO'),
            ('SOLIDAS','SOLIDAS'),
            ('TRICOLOR','TRICOLOR'),
            ('UVA','UVA'),
            ('VARIADAS','VARIADAS'),
            ('VERDE','VERDE'),
            ('VERMELHO','VERMELHO'),
            ('VINHO','VINHO'),
        )

    PORTAS = (
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
        )

    tipo = models.CharField(max_length=20, choices=TIPO, null=False, blank=False,help_text='selecione Tipo do Veículo' )
    marca = models.CharField(max_length=20, choices=MARCAS, null=False, blank=False, help_text='selecione Marca' )
    modelo = models.CharField(max_length=50, null=False, blank=False, help_text='digite Modelo')
    ano_fabricacao = models.CharField(max_length=4,choices=ANO, default=2021, null=False, blank=False)
    ano_modelo = models.CharField(max_length=4,choices=ANO,default=2021,null=False, blank=False)
    combustível = models.CharField(max_length=20, choices=COMBUSTIVEL, null=False, blank=False)
    km = models.CharField(max_length=6,  null=True, blank=True)
    cambio = models.CharField(max_length=20,choices=CAMBIO, null=False, blank=False)
    cor = models.CharField(max_length=20, choices=CORES, null=False, blank=False)
    portas = models.CharField(max_length=1, choices=PORTAS, null=True, blank=False)
    valor = models.CharField(max_length=9, null=False, blank=False,help_text='no formato 1.000,00')
    contato = models.CharField(max_length=20, null=False, blank=False,help_text='         Número de WhatsApp')
    anunciante = models.CharField(null=False, max_length=20, blank=False,help_text='Nome')
    acessórios_opcionais = models.TextField(max_length=150 , null=True, blank=False,help_text='digite acessários opcionais tais como Alarme, KitMultimída, Som e Rodas.')
    imagem1 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
    imagem2 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
    imagem3 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
    imagem4 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
    imagem5 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
    imagem6 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=True)
    imagem7 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=True,blank=True)
    imagem8 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=True,blank=True)
    imagem9 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG',null=True,blank=True)
    imagem10 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=True,blank=True)
    


    def publish(self):
        self.save()

    def __str__(self):
        return self.marca
