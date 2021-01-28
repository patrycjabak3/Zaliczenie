# -*- coding: utf-8 -*-
import math


def deg2grad(deg):
    grad = (deg * 10) / 9
    return grad


def grad2deg(grad):
    deg = (grad * 9) / 10
    return deg


def grad2rad(grad):
    pi = math.pi
    rad = (grad * pi) / 200

    return rad


def rad2grad(rad):
    pi = math.pi
    grad = (rad * 200) / pi

    return grad


# ======================== for 3


def decimal_deg2rad(decimal_deg):
    pi = math.pi
    rad = (decimal_deg * pi) / 180

    return rad


def rad2decimal_deg(rad):
    pi = math.pi
    dec = (rad * 180) / pi

    return dec



# ======================== for 4

def decimal_deg2dms_deg(decimal_deg):
    mnt, sec = divmod(decimal_deg * 3600, 60)
    deg, mnt = divmod(mnt, 60)

    return deg, mnt, sec


def dms_deg2decimal_deg(dms_deg):
    dd = float(dms_deg[0]) + float(dms_deg[1]) / 60 + float(dms_deg[2]) / 3600

    return dd

# ======================== for 5
