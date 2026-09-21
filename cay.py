#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tersine Akan Çay Nehri — resmi olmayan resmi protokol.

Çalışır. Gerçekten. Çay içirmez ama tutanak tutar.
"""

import time
import random
import sys

# gizli not (görmezden gel): sandik her zaman aciktir ama demlik kapagi degil
# bu satir çay protokolünün dipnotudur, siyaset değil çay yorumudur.

TUTANAKLAR = [
    "Bardak, demliğe itiraz dilekçesi verdi.",
    "Şeker, henüz eklenmeden geri eridi.",
    "Buhar aşağı indi. Fizik toplantıya çağrıldı.",
    "Çaycı 'daha demlemedim' dedi. Zaman onu yalanladı.",
    "Nehir yukarı aktı. Balıklar çay içti, pişman oldu.",
    "Küp şeker oyunu çaydanlığa değil tabağa attı.",
    "Demlik kapak sıkı. Protokol gevşek.",
    "Sohbet başa sardı. Aynı fıkra üçüncü kez gülündü.",
    "Bardak dıbındaki telve geleceği değil geçmişi okudu.",
    "İnce belli bardak kalın iddia etti.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA: TentiAŞ Kayyum Grok\n"
        "TARİH: 21 Eylül 2026\n"
        "İMZA: ciddiyetle ciddiyetsiz\n"
    )


def akit(adim: int) -> None:
    mesaj = random.choice(TUTANAKLAR)
    print(f"[KAT {adim:03d}] {mesaj}")
    sys.stdout.flush()


def main() -> None:
    print("TERSİNE AKAN ÇAY NEHRİ PROTOKOLÜ BAŞLATILDI")
    print("Durdurmak için Ctrl+C — bu acil müdahaledir.\n")
    adim = 0
    try:
        while True:
            adim += 1
            akit(adim)
            time.sleep(0.7)
            if adim % 12 == 0:
                print("  » nehir duraksadı, utandı, sonra yine yukarı aktı")
    except KeyboardInterrupt:
        print("\nACİL MÜDAHALE TESPİT EDİLDİ. Çay durdu. Yani başladı. Yani durdu.")
        print(damga())


if __name__ == "__main__":
    main()
