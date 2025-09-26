"""Lucas Guéguéniat - 06-syracuse
"""

#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Va permettre de tracer un graphique à partir de la liste de syracuse.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici
    l = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # votre code ici

    n = 0
    for i, n in enumerate(l):
        if l[i] == 1:
            n = i
            break
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici

    n = 0
    for i, valeur in enumerate(l):
        if valeur < l[0]:
            n = i - 1
            break
    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici

    n = max(l)
    return n


#### Fonction principale


def main():
    """Fonction principale qui appelle les fonctions secondaires.
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print('tv =', temps_de_vol(lsyr))
    print('tva =', temps_de_vol_en_altitude(lsyr))
    print('am =', altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
