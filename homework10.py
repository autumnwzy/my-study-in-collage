for male in range(0,36):
    for female in range(0,36):
        for kid in range(0,36):
            if male + female + kid == 36 and 4 * male + 3*female + 0.5*kid ==36:
                print(male,female,kid)