#!/usr/bin/env python3
# coding: UTF-8
import sys
l1l11_opy_ = sys.version_info [0] == 2
l1l1_opy_ = 2048
l11ll_opy_ = 7
def l1_opy_ (keyedStringLiteral):
    global ll_opy_
    stringNr = ord (keyedStringLiteral [-1])
    rotatedStringLiteral = keyedStringLiteral [:-1]
    rotationDistance = stringNr % len (rotatedStringLiteral)
    recodedStringLiteral = rotatedStringLiteral [:rotationDistance] + rotatedStringLiteral [rotationDistance:]
    if l1l11_opy_:
        stringLiteral = unicode () .join ([unichr (ord (char) - l1l1_opy_ - (charIndex + stringNr) % l11ll_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    else:
        stringLiteral = str () .join ([chr (ord (char) - l1l1_opy_ - (charIndex + stringNr) % l11ll_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    return eval (stringLiteral)
import os, sys, re
l1111_opy_ = 40 + 1 + 9 + 4
l11l_opy_ = 0xFFFF
l1lll_opy_ = re.compile(l1_opy_ (u"ࠫࡤࡥࡖ࠴ࡆࡏࡣࡤ࠮࡛ࡢ࠯ࡩࡅ࠲ࡌ࠰࠮࠻ࡠࡿ࠶࠶ࠬ࠲࠲ࢀ࠭ࠬࠀ"))
def l111l_opy_(key):
    if len(key) != l1111_opy_:
        return False
    sum = 0
    for i in range(len(key) - 4):
        sum = sum + ord(key[i])
    l1l_opy_ = sum % l11l_opy_
    l11_opy_ = int(key[len(key)-4 : ], 16)
    return l1l_opy_ == l11_opy_
def check_key(key):
    return l111l_opy_(key)
def verify(path):
    with open(path, l1_opy_ (u"ࠬࡸࠧࠁ"),  encoding=l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬࠂ")) as l1llll_opy_:
        file = l1llll_opy_.read()
        match = l1lll_opy_.search(file)
        if match and match.group(1) != l1_opy_ (u"ࠧ࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳ࠫࠃ"):
            return True
        else:
            return False
def activate(path, key, l1ll_opy_=True):
    if l1ll_opy_ and not l111l_opy_(key):
        return False
    l1ll1_opy_ = l1_opy_ (u"ࠨࡡࡢ࡚࠸ࡊࡌࡠࡡࠪࠄ") + key[0:10]
    file = None
    with open(path, l1_opy_ (u"ࠩࡵࠫࠅ"),  encoding=l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩࠆ")) as l1llll_opy_:
        file = l1llll_opy_.read()
    with open(path, l1_opy_ (u"ࠫࡼ࠭ࠇ"),  encoding=l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫࠈ")) as l1l1l_opy_:
        l1l1l_opy_.write(l1lll_opy_.sub(l1ll1_opy_, file))
    return True
def deactivate(path):
    return activate(path, l1_opy_ (u"࠭࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲ࠪࠉ"), False)
if __name__ == l1_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩࠊ"):
    l111_opy_ = sys.argv
    if len(l111_opy_) < 3:
        sys.exit(1)
    else:
        l11l1_opy_ = l111_opy_[1]
        if (l11l1_opy_ == l1_opy_ (u"ࠨࡥ࡫ࡩࡨࡱ࠭࡬ࡧࡼࠫࠋ") or l11l1_opy_ == l1_opy_ (u"ࠩࡦ࡬ࡪࡩ࡫ࡠ࡭ࡨࡽࠬࠌ")) and len(l111_opy_) == 3:
            if check_key(l111_opy_[2]):
                print(l1_opy_ (u"ࠪࡓࡐ࠭ࠍ"))
                sys.exit(0)
            else:
                print(l1_opy_ (u"ࠫࡇࡇࡄࠨࠎ"))
                sys.exit(1)
        elif l11l1_opy_ == l1_opy_ (u"ࠬࡼࡥࡳ࡫ࡩࡽࠬࠏ") and len(l111_opy_) == 3:
            if verify(l111_opy_[2]):
                print(l1_opy_ (u"࠭ࡏࡌࠩࠐ"))
                sys.exit(0)
            else:
                print(l1_opy_ (u"ࠧࡃࡃࡇࠫࠑ"))
                sys.exit(1)
        elif l11l1_opy_ == l1_opy_ (u"ࠨࡣࡦࡸ࡮ࡼࡡࡵࡧࠪࠒ") and len(l111_opy_) == 4:
            activate(l111_opy_[2], l111_opy_[3])
            sys.exit(0)
        elif l11l1_opy_ == l1_opy_ (u"ࠩࡧࡩࡦࡩࡴࡪࡸࡤࡸࡪ࠭ࠓ") and len(l111_opy_) == 3:
            deactivate(l111_opy_[2])
            sys.exit(0)
        else:
            sys.exit(1)