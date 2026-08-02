"""
data/real_sample/registry.py
-------------------------------
Central list of every real player collected so far via Baseball Savant
screenshots. Adding a new player = add their _savant_2026.py file next to
this one, then add one line here. Everything downstream (validation,
raw_players.csv/raw_batted_balls.csv builder) reads from this list, so
nothing else needs to change as the roster grows.
"""

from judge_savant_2026 import JUDGE_2026_SNAPSHOT
from stanton_savant_2026 import STANTON_2026_SNAPSHOT
from cruz_savant_2026 import CRUZ_2026_SNAPSHOT
from tatis_savant_2026 import TATIS_2026_SNAPSHOT
from schwarber_savant_2026 import SCHWARBER_2026_SNAPSHOT
from alonso_savant_2026 import ALONSO_2026_SNAPSHOT
from alvarez_savant_2026 import ALVAREZ_2026_SNAPSHOT
from delacruz_savant_2026 import DELACRUZ_2026_SNAPSHOT
from arraez_savant_2026 import ARRAEZ_2026_SNAPSHOT
from kwan_savant_2026 import KWAN_2026_SNAPSHOT
from hoerner_savant_2026 import HOERNER_2026_SNAPSHOT
from altuve_savant_2026 import ALTUVE_2026_SNAPSHOT
from freeman_savant_2026 import FREEMAN_2026_SNAPSHOT
from soto_savant_2026 import SOTO_2026_SNAPSHOT
from witt_savant_2026 import WITT_2026_SNAPSHOT
from acuna_savant_2026 import ACUNA_2026_SNAPSHOT
from carroll_savant_2026 import CARROLL_2026_SNAPSHOT
from henderson_savant_2026 import HENDERSON_2026_SNAPSHOT
from rutschman_savant_2026 import RUTSCHMAN_2026_SNAPSHOT
from turang_savant_2026 import TURANG_2026_SNAPSHOT
from abreu_savant_2026 import ABREU_2026_SNAPSHOT
from caminero_savant_2026 import CAMINERO_2026_SNAPSHOT
from wood_savant_2026 import WOOD_2026_SNAPSHOT
from chourio_savant_2026 import CHOURIO_2026_SNAPSHOT
from merrill_savant_2026 import MERRILL_2026_SNAPSHOT
from dominguez_savant_2026 import DOMINGUEZ_2026_SNAPSHOT
from walker_savant_2026 import WALKER_2026_SNAPSHOT
from langford_savant_2026 import LANGFORD_2026_SNAPSHOT
from turner_savant_2026 import TURNER_2026_SNAPSHOT
from lindor_savant_2026 import LINDOR_2026_SNAPSHOT
from abrams_savant_2026 import ABRAMS_2026_SNAPSHOT
from marte_savant_2026 import MARTE_2026_SNAPSHOT
from robert_savant_2026 import ROBERT_2026_SNAPSHOT
from castellanos_savant_2026 import CASTELLANOS_2026_SNAPSHOT
from albies_savant_2026 import ALBIES_2026_SNAPSHOT
from bogaerts_savant_2026 import BOGAERTS_2026_SNAPSHOT
from olson_savant_2026 import OLSON_2026_SNAPSHOT
from ozuna_savant_2026 import OZUNA_2026_SNAPSHOT
from ohtani_savant_2026 import OHTANI_2026_SNAPSHOT
from devers_savant_2026 import DEVERS_2026_SNAPSHOT
from contreras_savant_2026 import CONTRERAS_2026_SNAPSHOT
from perez_savant_2026 import PEREZ_2026_SNAPSHOT
from betts_savant_2026 import BETTS_2026_SNAPSHOT

REAL_PLAYER_SNAPSHOTS = [
    JUDGE_2026_SNAPSHOT,
    STANTON_2026_SNAPSHOT,
    CRUZ_2026_SNAPSHOT,
    TATIS_2026_SNAPSHOT,
    SCHWARBER_2026_SNAPSHOT,
    ALONSO_2026_SNAPSHOT,
    ALVAREZ_2026_SNAPSHOT,
    DELACRUZ_2026_SNAPSHOT,
    ARRAEZ_2026_SNAPSHOT,
    KWAN_2026_SNAPSHOT,
    HOERNER_2026_SNAPSHOT,
    ALTUVE_2026_SNAPSHOT,
    FREEMAN_2026_SNAPSHOT,
    SOTO_2026_SNAPSHOT,
    WITT_2026_SNAPSHOT,
    ACUNA_2026_SNAPSHOT,
    CARROLL_2026_SNAPSHOT,
    HENDERSON_2026_SNAPSHOT,
    RUTSCHMAN_2026_SNAPSHOT,
    TURANG_2026_SNAPSHOT,
    ABREU_2026_SNAPSHOT,
    CAMINERO_2026_SNAPSHOT,
    WOOD_2026_SNAPSHOT,
    CHOURIO_2026_SNAPSHOT,
    MERRILL_2026_SNAPSHOT,
    DOMINGUEZ_2026_SNAPSHOT,
    WALKER_2026_SNAPSHOT,
    LANGFORD_2026_SNAPSHOT,
    TURNER_2026_SNAPSHOT,
    LINDOR_2026_SNAPSHOT,
    ABRAMS_2026_SNAPSHOT,
    MARTE_2026_SNAPSHOT,
    ROBERT_2026_SNAPSHOT,
    CASTELLANOS_2026_SNAPSHOT,
    ALBIES_2026_SNAPSHOT,
    BOGAERTS_2026_SNAPSHOT,
    OLSON_2026_SNAPSHOT,
    OZUNA_2026_SNAPSHOT,
    OHTANI_2026_SNAPSHOT,
    DEVERS_2026_SNAPSHOT,
    CONTRERAS_2026_SNAPSHOT,
    PEREZ_2026_SNAPSHOT,
    BETTS_2026_SNAPSHOT,
]

# Judge/Stanton were already-collected "bonus" players (also validated via a
# real GitHub batted-ball export), so the original 30-name list target maps
# to 32 total in this registry. Betts (added here) completes that list.
# Marte/Robert/Castellanos/Albies/Olson/Ozuna/Ohtani/Devers/Contreras/Perez
# are extras added afterward to fill profile gaps (contact-extreme, low
# bat speed, power-extreme, catchers), so the registry now runs well ahead
# of the original 32-name target.
TARGET_ROSTER_SIZE = 32


def status():
    n = len(REAL_PLAYER_SNAPSHOTS)
    names = ", ".join(s["player_name"] for s in REAL_PLAYER_SNAPSHOTS)
    print(f"Jugadores reales recolectados: {n}/{TARGET_ROSTER_SIZE}")
    print(f"  {names}")
    print(f"  Faltan {max(0, TARGET_ROSTER_SIZE - n)} para poder reemplazar el dataset simulado.")


if __name__ == "__main__":
    status()
