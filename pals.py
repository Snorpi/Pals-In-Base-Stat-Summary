class Character:
    def __init__(self, pal_number, pal_name, kindling, planting, handiwork, lumbering, medicine_production,
                 transporting,
                 watering, generating_electricity, gathering, mining, cooling, farming):
        self.pal_number = pal_number
        self.pal_name = pal_name
        self.kindling = kindling
        self.planting = planting
        self.handiwork = handiwork
        self.lumbering = lumbering
        self.medicine_production = medicine_production
        self.transporting = transporting
        self.watering = watering
        self.generating_electricity = generating_electricity
        self.gathering = gathering
        self.mining = mining
        self.cooling = cooling
        self.farming = farming


characters = [
    Character(1, "Lamball", 0, 0, 1, 0, 0,
              1, 0, 0, 0, 0, 0, 1),
    Character('2', 'Cattiva', 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0),
    Character('3', 'Chikipi', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
    Character('4', 'Lifmunk', 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0),
    Character('5', 'Foxparks', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('6', 'Fuack', 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0),
    Character('7', 'Sparkit', 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0),
    Character('8', 'Tanzee', 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0),
    Character('9', 'Rooby', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('10', 'Pengullet', 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0),
    Character('11', 'Penking', 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0),
    Character('12', 'Jolthog', 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    Character('13', 'Gumoss', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('14', 'Vixy', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
    Character('15', 'Hoocrates', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Character('16', 'Teafant', 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    Character('17', 'Depresso', 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0),
    Character('18', 'Cremis', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
    Character('19', 'Daedream', 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0),
    Character('20', 'Rushoar', 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    Character('21', 'Nox', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Character('22', 'Fuddler', 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0),
    Character('23', 'Killamari', 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0),
    Character('24', 'Mau', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    Character('25', 'Celaray', 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0),
    Character('26', 'Direhowl', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Character('27', 'Tocotoco', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Character('28', 'Flopie', 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0),
    Character('29', 'Mozzarina', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    Character('30', 'Bristla', 0, 1, 1, 0, 2, 1, 0, 0, 1, 0, 0, 0),
    Character('31', 'Gobfin', 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0),
    Character('32', 'Hangyu', 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0),
    Character('33', 'Mossanda', 0, 2, 2, 2, 0, 3, 0, 0, 0, 0, 0, 0),
    Character('34', 'Woolipop', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    Character('35', 'Caprity', 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    Character('36', 'Melpaca', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    Character('37', 'Eikthyrdeer', 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('38', 'Nitewing', 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0),
    Character('39', 'Ribbuny', 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0),
    Character('40', 'Incineram', 1, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0),
    Character('41', 'Cinnamoth', 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    Character('42', 'Arsox', 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('43', 'Dumud', 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 0, 0),
    Character('44', 'Cawgnito', 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('45', 'Leezpunk', 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0),
    Character('46', 'Loupmoon', 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('47', 'Galeclaw', 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0),
    Character('48', 'Robinquill', 0, 1, 2, 1, 1, 2, 0, 0, 2, 0, 0, 0),
    Character('49', 'Gorirat', 0, 0, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0),
    Character('50', 'Beegarde', 0, 1, 1, 1, 1, 2, 0, 0, 1, 0, 0, 1),
    Character('51', 'Elizabee', 0, 2, 2, 1, 1, 2, 0, 0, 2, 0, 0, 1),
    Character('52', 'Grintale', 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0),
    Character('53', 'Swee', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    Character('54', 'Sweepa', 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0),
    Character('55', 'Chillet', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    Character('56', 'Univolt', 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0),
    Character('57', 'Foxcicle', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    Character('58', 'Pyrin', 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('59', 'Reindrix', 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0),
    Character('60', 'Rayhound', 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0),
    Character('61', 'Kitsun', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('62', 'Dazzi', 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0),
    Character('63', 'Lunaris', 0, 0, 3, 0, 0, 1, 0, 0, 1, 0, 0, 0),
    Character('64', 'Dinossom', 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('65', 'Surfent', 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0),
    Character('66', 'Maraith', 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0),
    Character('67', 'Digtoise', 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0),
    Character('68', 'Tombat', 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0),
    Character('69', 'Lovander', 0, 0, 2, 0, 2, 2, 0, 0, 0, 1, 0, 0),
    Character('70', 'Flambelle', 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1),
    Character('71', 'Vanwyrm', 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0),
    Character('72', 'Bushi', 2, 0, 1, 3, 0, 2, 0, 0, 1, 0, 0, 0),
    Character('73', 'Beakon', 0, 0, 0, 0, 0, 3, 0, 2, 1, 0, 0, 0),
    Character('74', 'Ragnahawk', 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0),
    Character('75', 'Katress', 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0),
    Character('76', 'Wixen', 2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0),
    Character('77', 'Verdash', 0, 2, 3, 2, 0, 2, 0, 0, 3, 0, 0, 0),
    Character('78', 'Vaelet', 0, 2, 2, 0, 3, 1, 0, 0, 3, 0, 0, 0),
    Character('79', 'Sibelyx', 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1),
    Character('80', 'Elphidran', 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('81', 'Kelpsea', 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    Character('82', 'Azurobe', 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0),
    Character('83', 'Cryolinx', 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 3, 0),
    Character('84', 'Blazehowl', 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('85', 'Relaxaurus', 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0),
    Character('86', 'Broncherry', 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('87', 'Petallia', 0, 3, 2, 0, 2, 1, 0, 0, 2, 0, 0, 0),
    Character('88', 'Reptyro', 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0),
    Character('89', 'Kingpaca', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Character('90', 'Mammorest', 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0),
    Character('91', 'Wumpo', 0, 0, 2, 3, 0, 4, 0, 0, 0, 0, 2, 0),
    Character('92', 'Warsect', 0, 1, 1, 3, 0, 3, 0, 0, 0, 0, 0, 0),
    Character('93', 'Fenglope', 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('94', 'Felbat', 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0),
    Character('95', 'Quivern', 0, 0, 1, 0, 0, 3, 0, 0, 2, 3, 0, 0),
    Character('96', 'Blazamut', 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0),
    Character('97', 'Helzephyr', 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0),
    Character('98', 'Astegon', 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0),
    Character('99', 'Menasting', 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0),
    Character('100', 'Anubis', 0, 0, 4, 0, 0, 2, 0, 0, 0, 3, 0, 0),
    Character('101', 'Jormuntide', 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0),
    Character('102', 'Suzaku', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('103', 'Grizzbolt', 0, 0, 2, 0, 0, 3, 0, 3, 2, 0, 0, 0),
    Character('104', 'Lyleen', 0, 4, 3, 0, 3, 0, 0, 0, 2, 0, 0, 0),
    Character('105', 'Faleris', 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0),
    Character('106', 'Orserk', 0, 0, 3, 0, 0, 3, 0, 4, 0, 0, 0, 0),
    Character('107', 'Shadowbeak', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Character('108', 'Paladius', 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0),
    Character('109', 'Necromus', 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0),
    Character('110', 'Frostallion', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0),
    Character('111', 'Jetragon', 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0),
    Character('101B', 'Jormuntide Ignis', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('102B', 'Suzaku Aqua', 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0),
    Character('104B', 'Lyleen Noct', 0, 0, 3, 0, 3, 0, 0, 0, 2, 0, 0, 0),
    Character('110B', 'Frostallion Noct', 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0),
    Character('12B', 'Jolthog Cryst', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    Character('24B', 'Mau Cryst', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    Character('31B', 'Gobfin Ignis', 2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    Character('32B', 'Hangyu Cryst', 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    Character('33B', 'Mossanda Lux', 0, 0, 2, 2, 0, 3, 0, 2, 0, 0, 0, 0),
    Character('38B', 'Eikthyrdeer Terra', 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('40B', 'Inceneram Noct', 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0),
    Character('45B', 'Leezpunk Ignis', 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0),
    Character('48B', 'Robinquill Terra', 0, 0, 2, 1, 1, 2, 0, 0, 2, 0, 0, 0),
    Character('58B', 'Pyrin Noct', 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('64B', 'Dinossom Lux', 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0),
    Character('65B', 'Surfent Terra', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Character('71B', 'Vanwyrm Cryst', 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0),
    Character('80B', 'Elphidran Aqua', 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0),
    Character('81B', 'Kelpsea Ignis', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('84B', 'Blazehowl Noct', 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Character('85B', 'Relaxaurus Lux', 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0),
    Character('86B', 'Broncherry Aqua', 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0),
    Character('88B', 'Ice Reptyro', 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0),
    Character('89B', 'Ice Kingpaca', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0),
    Character('90B', 'Mammorest Cryst', 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0),
    Character('91B', 'Wumpo Botan', 0, 1, 2, 3, 0, 4, 0, 0, 0, 0, 0, 0)
]