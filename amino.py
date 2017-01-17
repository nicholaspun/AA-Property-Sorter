def extractprop(sequence):
# [listof char] -> ([listof char], [listof char], [listof char])
# extractprop(sequence) produces a tuple containing a list of
#   charged AA's, polar AA's and hydro AA's, in that order.

    charged = []
    polar = []
    hydro = []

    for i in range(len(sequence)):
        aa = sequence[i]
        if (aa in 'RKDE'):
            charged.append(aa)
        elif (aa in 'QNHSTYCMW'):
            polar.append(aa)
        elif (aa in 'AILFVPG'):
            hydro.append(aa)
        else:
            continue

    return (charged, polar, hydro)

