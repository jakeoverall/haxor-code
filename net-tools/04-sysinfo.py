import psutil

times = psutil.cpu_times()


print(f"""

-----------System Info----------

  [~] User Time: {times.user}
  [~] System Time: {times.system}
  [~] Interrupt Time: {times.interrupt}
  [~] Idle Time: {times.idle}

-----------End System Info----------

""")
