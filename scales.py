NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
SEMI = 1
TONE = 2
MAJOR = [TONE, TONE, SEMI, TONE, TONE, TONE, SEMI]
MINOR = [TONE, SEMI, TONE, TONE, SEMI, TONE, TONE]

def calculate_major_scale(root_note):

    major_scale = [root_note]
    index = NOTES.index(root_note)
    for interval in MAJOR:
        index = (index + interval) % 12
        major_scale.append(NOTES[index])

    return major_scale

def calculate_minor_scale(root_note):

    minor_scale = [root_note]
    index = NOTES.index(root_note)
    for interval in MINOR:
        index = (index + interval) % 12
        minor_scale.append(NOTES[index])

    return minor_scale

root_note = input("Root note: ")
print(f"major: {calculate_major_scale(root_note)}")
print(f"minor: {calculate_minor_scale(root_note)}")