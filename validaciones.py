def validar_tlim(string: str) -> bool:
    '''
    Valida si el argumento string representa un validor válido para TLim.
    '''
    try:
        tlim = float(string)
        if tlim <= 0:
            return False
    except ValueError:
        return False
    else:
        return True

def validar_pcl(string: str) -> bool:
    '''
    Valida si el argumento string representa un validor válido para PCl.
    '''
    try:
        pcl = int(string)
        if pcl <= 0:
            return False
    except ValueError:
        return False
    else:
        return True

def formatear_hora(tiempo: float) -> str:
    '''
    Recibe un tiempo en minutos y regresa un string en formato de hora.
    '''
    horas = tiempo / 60
    minutos = (horas % 1) * 60
    segundos = (minutos % 1) * 60

    str_horas = f'{int(horas)} h ' if horas >= 1 else ''
    str_minutos = f'{int(minutos)} m ' if minutos >= 1 else ''
    str_segundos = f'{int(segundos)} s' if segundos >= 1 else ''

    return f'{str_horas}{str_minutos}{str_segundos}'
