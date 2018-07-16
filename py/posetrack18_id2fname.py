import os

posetrack17_train_sequences = set(
    [
        (1, 8838),
        (1, 12218),
        (1, 6852),
        (1, 16530),
        (1, 12507),
        (1, 14073),
        (1, 9488),
        (1, 22683),
        (1, 16637),
        (1, 7861),
        (1, 8968),
        (1, 43),
        (1, 8732),
        (1, 13627),
        (1, 7380),
        (1, 13780),
        (1, 2716),
        (1, 98),
        (1, 436),
        (1, 14265),
        (1, 17133),
        (1, 16464),
        (1, 9922),
        (1, 10773),
        (1, 7607),
        (1, 228),
        (1, 20924),
        (1, 24635),
        (1, 16571),
        (1, 760),
        (1, 14321),
        (1, 16165),
        (1, 8808),
        (1, 23492),
        (1, 866),
        (1, 6265),
        (1, 16882),
        (1, 275),
        (1, 24985),
        (1, 2905),
        (1, 20928),
        (1, 7851),
        (1, 3402),
        (1, 16171),
        (1, 15882),
        (1, 823),
        (1, 3498),
        (1, 14344),
        (1, 14354),
        (1, 20900),
        (1, 9533),
        (2, 10),
        (1, 14480),
        (1, 15892),
        (1, 3701),
        (1, 15124),
        (1, 16411),
        (1, 9043),
        (1, 9012),
        (1, 8743),
        (1, 12620),
        (2, 28),
        (1, 16440),
        (1, 7855),
        (1, 15130),
        (1, 271),
        (1, 8820),
        (1, 15875),
        (1, 23471),
        (1, 8882),
        (1, 2357),
        (1, 24180),
        (2, 15),
        (1, 23695),
        (1, 16883),
        (1, 231),
        (1, 15290),
        (1, 13337),
        (1, 9003),
        (1, 13908),
        (1, 3403),
        (2, 1),
        (1, 502),
        (1, 9495),
        (1, 14268),
        (1, 8961),
        (1, 15277),
        (1, 8616),
        (1, 14345),
        (1, 14278),
        (1, 985),
        (1, 1243),
        (1, 11989),
        (1, 15125),
        (1, 13515),
        (2, 29),
        (1, 2839),
        (1, 15366),
        (1, 13821),
        (1, 9718),
        (1, 12056),
        (1, 14052),
        (1, 21077),
        (1, 12268),
        (1, 5728),
        (1, 21133),
        (1, 8819),
        (1, 13965),
        (1, 5759),
        (1, 17180),
        (1, 14553),
        (1, 9506),
        (1, 22671),
        (1, 5847),
        (1, 10288),
        (1, 22682),
        (1, 14231),
        (1, 8969),
        (1, 14403),
        (1, 20896),
        (1, 7381),
        (1, 14375),
        (1, 14122),
        (1, 16535),
        (1, 1158),
        (1, 14506),
        (1, 9598),
        (1, 14334),
        (1, 17184),
        (1, 2893),
        (1, 23699),
        (1, 10010),
        (1, 3730),
        (1, 12023),
        (2, 48),
        (1, 23454),
        (1, 9499),
        (1, 9654),
        (1, 14235),
        (1, 10111),
        (1, 13795),
        (1, 16496),
        (1, 16313),
        (1, 8795),
        (1, 12732),
        (1, 9534),
        (2, 17),
        (1, 439),
        (1, 8744),
        (1, 1682),
        (1, 921),
        (1, 8833),
        (1, 14054),
        (1, 4902),
        (1, 24893),
        (2, 3),
        (1, 10715),
        (1, 15309),
        (1, 820),
        (1, 10542),
        (1, 285),
        (1, 7467),
        (1, 13271),
        (1, 15406),
        (1, 9487),
        (1, 14763),
        (1, 12155),
        (1, 9398),
        (1, 1686),
        (1, 2255),
        (1, 8837),
        (1, 2787),
        (1, 12911),
        (1, 9054),
        (1, 223),
        (1, 14662),
        (1, 12722),
        (2, 27),
        (1, 15585),
        (1, 4833),
        (1, 14551),
        (1, 9504),
        (1, 9555),
        (1, 13787),
        (1, 9993),
        (1, 14363),
        (1, 8803),
        (1, 9411),
        (1, 15189),
        (1, 9617),
        (1, 8725),
        (1, 4891),
        (1, 14390),
        (1, 20822),
        (1, 5732),
        (1, 12859),
        (1, 474),
        (1, 2552),
        (1, 10774),
        (1, 14367),
        (2, 23),
        (1, 520),
        (1, 14272),
        (1, 13527),
        (1, 2234),
        (1, 5841),
        (1, 15899),
        (1, 9538),
        (1, 14266),
        (1, 15537),
        (1, 13671),
        (1, 7387),
        (1, 8906),
        (2, 26),
        (1, 10198),
        (1, 7413),
        (1, 2258),
        (1, 14082),
        (1, 16215),
        (1, 15314),
        (1, 12273),
        (1, 17121),
        (1, 20823),
        (1, 14183),
        (1, 15765),
        (1, 11280),
        (1, 16433),
        (1, 23416),
        (1, 8730),
        (1, 21078),
        (1, 352),
        (1, 17197),
        (1, 14121),
        (1, 22676),
        (1, 14505),
        (1, 14280),
        (1, 4836),
        (2, 22),
        (1, 16198),
        (1, 7392),
        (1, 9445),
        (1, 13268),
        (1, 16211),
        (1, 2264),
        (1, 24487),
        (1, 14698),
        (1, 10007),
        (1, 8812),
        (2, 36),
        (1, 8796),
        (1, 16330),
        (1, 9938),
        (1, 96),
        (1, 17129),
        (1, 8976),
        (1, 22642),
        (1, 7536),
        (1, 385),
        (1, 16417),
        (1, 9597),
        (1, 13512),
        (1, 1157),
        (1, 15293),
        (1, 14178),
        (1, 13557),
        (1, 14129),
        (1, 1491),
        (1, 8877),
        (1, 23484),
        (2, 2),
        (1, 10177),
        (1, 10863),
        (1, 8884),
        (1, 8962),
        (1, 5061),
        (1, 2843),
        (1, 9727),
        (1, 24642),
        (1, 14288),
        (1, 1153),
        (1, 15832),
        (1, 1687),
        (1, 2254),
        (1, 15177),
        (1, 2786),
        (1, 12910),
        (1, 22124),
        (1, 1341),
        (1, 16668),
        (1, 14342),
        (1, 5232),
        (1, 799),
    ]
)

posetrack17_testval_sequences = set(
    [
        (1, 707),
        (1, 11878),
        (1, 16842),
        (1, 5368),
        (1, 286),
        (1, 9528),
        (1, 8993),
        (1, 9038),
        (1, 9468),
        (1, 10127),
        (1, 18900),
        (1, 16611),
        (1, 14361),
        (1, 46),
        (1, 15869),
        (1, 1110),
        (1, 23966),
        (1, 475),
        (1, 18906),
        (1, 20856),
        (1, 229),
        (1, 3136),
        (1, 13029),
        (1, 1757),
        (1, 24566),
        (1, 24153),
        (1, 16451),
        (1, 2838),
        (1, 2266),
        (1, 903),
        (1, 14703),
        (1, 17496),
        (1, 15755),
        (1, 14027),
        (1, 750),
        (1, 3745),
        (3, 2),
        (1, 16235),
        (1, 12967),
        (1, 10130),
        (1, 15294),
        (1, 17447),
        (1, 16517),
        (1, 15521),
        (1, 13601),
        (1, 14376),
        (1, 15149),
        (1, 18719),
        (1, 14313),
        (1, 1970),
        (1, 8894),
        (1, 14292),
        (1, 10309),
        (1, 19980),
        (1, 6503),
        (1, 3504),
        (1, 9472),
        (1, 8826),
        (1, 24177),
        (1, 17434),
        (3, 3),
        (1, 2061),
        (1, 24493),
        (1, 6545),
        (1, 3542),
        (1, 24906),
        (1, 9268),
        (1, 18592),
        (1, 9469),
        (1, 17955),
        (1, 21082),
        (1, 22831),
        (1, 21130),
        (1, 2284),
        (1, 808),
        (1, 15868),
        (1, 21084),
        (1, 12046),
        (1, 1733),
        (1, 24149),
        (1, 12332),
        (1, 17984),
        (1, 11526),
        (1, 2928),
        (1, 5803),
        (1, 23411),
        (1, 15941),
        (1, 2777),
        (1, 16556),
        (1, 9301),
        (1, 23746),
        (1, 18159),
        (1, 10303),
        (1, 9523),
        (1, 22892),
        (1, 10521),
        (1, 18626),
        (1, 7504),
        (1, 18412),
        (1, 1535),
        (1, 14309),
        (1, 1280),
        (1, 15862),
        (1, 2367),
        (1, 22656),
        (1, 3397),
        (1, 14524),
        (1, 18657),
        (1, 9452),
        (1, 8991),
        (1, 5413),
        (1, 3223),
        (1, 9509),
        (1, 8736),
        (1, 10357),
        (1, 20912),
        (1, 161),
        (1, 18296),
        (1, 44),
        (1, 2281),
        (1, 20909),
        (1, 7269),
        (1, 16421),
        (1, 22693),
        (3, 1),
        (1, 14522),
        (1, 15375),
        (1, 24564),
        (1, 1940),
        (1, 14297),
        (1, 19078),
        (1, 15908),
        (1, 16419),
        (1, 9477),
        (1, 2273),
        (1, 7952),
        (1, 24573),
        (1, 9460),
        (3, 5),
        (1, 16576),
        (1, 14317),
        (1, 11287),
        (1, 16194),
        (1, 7681),
        (1, 9458),
        (1, 12838),
        (1, 5799),
        (1, 18623),
        (1, 8761),
        (1, 24516),
        (1, 8160),
        (1, 9526),
        (1, 15859),
        (1, 20818),
        (1, 9403),
        (1, 2279),
        (1, 3416),
        (1, 202),
        (1, 20820),
        (1, 22699),
        (1, 24156),
        (1, 1545),
        (1, 23730),
        (1, 5336),
        (1, 1242),
        (1, 693),
        (1, 14307),
        (1, 15812),
        (3, 4),
        (1, 9602),
        (1, 23444),
        (1, 6818),
        (1, 8847),
        (1, 21086),
        (1, 2286),
        (1, 10517),
        (1, 3546),
        (1, 23965),
        (1, 23736),
        (1, 2852),
        (1, 10350),
        (1, 536),
        (1, 9476),
        (1, 811),
        (1, 3224),
        (1, 83),
        (1, 24876),
        (1, 9404),
        (1, 9521),
        (1, 23719),
        (1, 7500),
        (1, 20819),
        (1, 9527),
        (1, 13602),
        (1, 1282),
        (1, 21123),
        (1, 15278),
        (1, 8789),
        (1, 1537),
        (1, 5592),
        (1, 13534),
        (1, 15302),
        (1, 24158),
        (1, 24621),
        (1, 7684),
        (1, 3742),
        (1, 16662),
        (1, 2276),
        (1, 1735),
        (1, 2835),
        (1, 16180),
        (1, 23717),
        (1, 20880),
        (1, 522),
        (1, 14102),
        (1, 14384),
        (1, 1001),
        (1, 1486),
        (1, 4622),
        (1, 14531),
        (1, 20910),
        (1, 8827),
        (1, 2277),
        (1, 14293),
        (1, 9883),
        (1, 16239),
        (1, 16236),
        (1, 8760),
        (1, 15860),
        (1, 7128),
        (1, 5833),
        (1, 23653),
        (1, 5067),
        (1, 14523),
        (1, 24165),
        (1, 18725),
        (1, 7496),
        (1, 342),
        (1, 17839),
        (1, 15301),
        (1, 24575),
        (1, 2364),
        (1, 1744),
        (1, 13293),
        (1, 14960),
        (1, 22430),
        (1, 23754),
        (1, 3943),
        (1, 12834),
        (1, 22688),
    ]
)


def idx2seqtype(idx):
    if idx == 1:
        return "mpii"
    elif idx == 2:
        return "bonn"
    elif idx == 3:
        return "mpiinew"
    else:
        assert False


def seqtype2idx(seqtype):
    if seqtype == "mpii":
        return 1
    elif seqtype == "bonn":
        return 2
    elif seqtype == "mpiinew":
        return 3
    else:
        assert False


def posetrack18_id2fname(image_id):
    """Generates filename given image id 

    Args:
      id: integer in the format TSSSSSSFFF, 
          T encodes the sequence source (1: 'mpii', 2: 'bonn', 3: 'mpiinew')
          SSSSSS is 6-digit index of the sequence
          FFF is 3-digit index of the image frame 
          
    Returns:
      name of the video sequence
    """
    seqtype_idx = image_id / 1000000000
    seqidx = (image_id % 1000000000) / 1000
    frameidx = image_id % 1000

    fname = "{:06}_{}_relpath_5sec".format(seqidx, idx2seqtype(seqtype_idx))

    if (seqtype_idx, seqidx) in posetrack17_testval_sequences:
        fname += "_testsub"
    else:
        assert (seqtype_idx, seqidx) in posetrack17_train_sequences
        fname += "_trainsub"

    return fname, frameidx


def posetrack18_fname2id(fname, frameidx):
    """Generates image id 

    Args:
      fname: name of the PoseTrack sequence
      frameidx: index of the frame within the sequence
    """
    tok = os.path.basename(fname).split("_")
    seqidx = int(tok[0])
    seqtype_idx = seqtype2idx(tok[1])

    assert frameidx >= 0 and frameidx < 1e3
    image_id = seqtype_idx * 1000000000 + seqidx * 1000 + frameidx
    return image_id
