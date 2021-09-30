from time import sleep
import os

T1, T2 = int(input("Skriv et ledd til å summere: ")), int(input("Skriv et annet ledd til å summere: "))

clear = lambda: os.system("cls" if os.name == "nt" else "clear")


def render_rutebok(rutebok):
  clear()
  for i in rutebok:
    print("".join(i))

farge_bla = "\033[94m"
farge_gronn = "\033[92m"
farge_gul = "\033[93m"
understrek = "\033[21m"

farge_escape = "\033[0m"


def strek_under_svar(rutebok):
  linje_index = -1
  for _ in range(len(rutebok[4])-2):
    rutebok[4][linje_index] = f"{understrek}{rutebok[4][linje_index]}"
    linje_index -= 1
  return rutebok


def addisjon_oppsett(t1, t2):
  string_tall = [t1, t2]
  string_tall = sorted(string_tall, reverse=True)
  string_tall = [str(_) for _ in string_tall]
  rutebok = [[" " for i in range(len(string_tall[0])+2)] for i in range(6)]

  rutebok[3][0] = f"{farge_bla}+{farge_escape}"
  rutebok[4][0] = f"{farge_bla}={farge_escape}"

  for rutebok_linje, tall in enumerate(string_tall, start=2):
    liste_tall = list(tall)
    liste_tall.reverse()
    rutebok_index = -1
    for i in liste_tall:
      rutebok[rutebok_linje][rutebok_index] = i
      rutebok_index -= 1
  render_rutebok(rutebok)

  svar_index = -1
  minnetall_index = -2
  tall_index = -1
  minnetall = False
  for i in range(1, len(string_tall[0])+1):
    try:
      svar = int(string_tall[0][tall_index]) + int(string_tall[1][tall_index])
    except IndexError:
        svar = int(string_tall[0][tall_index])
    if minnetall:
        svar += 1
    minnetall = False
    if svar > 9:
      svar -= 10
      minnetall = True 

    rutebok[4][svar_index] = f"{farge_gronn}{svar}{farge_escape}"
    yield rutebok
    if minnetall:
      if i == len(string_tall[0]):
          rutebok[4][svar_index-1] = "1"   
      else:
          rutebok[1][minnetall_index] = f"{farge_gul}1{farge_escape}"
      yield rutebok

    svar_index -= 1
    minnetall_index -= 1
    tall_index -= 1

  render_rutebok(rutebok)
        


  


if __name__ == '__main__':
  for steg in addisjon_oppsett(T1, T2):
      render_rutebok(steg)
      sleep(1)
  render_rutebok(strek_under_svar(steg))
  