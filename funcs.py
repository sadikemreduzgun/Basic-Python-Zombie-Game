def zombi_oldur(mermi_yx, mermi_yy, mermi_dx, mermi_dy, zombi_x, zombi_y):

    if (zombi_x<mermi_yx<zombi_x+25) and (zombi_y<mermi_yy<zombi_y+25):
        return False

    if (zombi_x<mermi_dx<zombi_x+25) and (zombi_y<mermi_dy<zombi_y+25):
        return False

    return True


def give_direc(x, y, zombi1_rast_x, zombi1_rast_y, zombi_hizi):

    zombi1_yon = "u"

    if (zombi1_rast_x - x) < 0:
        zombi1_rast_x += zombi_hizi
        # screen.blit(zombi_sag, (zombi1_rast_x, zombi1_rast_y))
        if (abs(zombi1_rast_x - x) - abs(zombi1_rast_y - y)) > 0:
            zombi1_yon = "r"

    else:
        zombi1_rast_x -= zombi_hizi
        if (abs(zombi1_rast_x - x) - abs(zombi1_rast_y - y)) > 0:
            zombi1_yon = "l"
        # screen.blit(zombi_sol, (zombi1_rast_x, zombi1_rast_y))
    if (zombi1_rast_y - y) < 0:
        zombi1_rast_y += zombi_hizi
        if (abs(zombi1_rast_x - x) - abs(zombi1_rast_y - y)) < 0:
            zombi1_yon = "d"
        # screen.blit(zombi_asagi, (zombi1_rast_x, zombi1_rast_y))
    else:
        zombi1_rast_y -= zombi_hizi
        if (abs(zombi1_rast_x - x) - abs(zombi1_rast_y - y)) < 0:
            zombi1_yon = "u"

    return zombi1_yon


def blit_iy(zombi1_yon, zombi_yukari, zombi_sol, zombi_sag, zombi_asagi,zombi1_rast_x, zombi1_rast_y, screen):
    if zombi1_yon == "u":
        screen.blit(zombi_yukari, (zombi1_rast_x, zombi1_rast_y))
    elif zombi1_yon == "l":
        screen.blit(zombi_sol, (zombi1_rast_x, zombi1_rast_y))
    elif zombi1_yon == "r":
        screen.blit(zombi_sag, (zombi1_rast_x, zombi1_rast_y))
    elif zombi1_yon == "d":
        screen.blit(zombi_asagi, (zombi1_rast_x, zombi1_rast_y))
