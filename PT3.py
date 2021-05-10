class Subjects:
    def subj(enrolled_subject):
        enrolled_subject.sub_1 = enrolled_subject.sub_2()
    def eli_subj(enrolled_subject):
        return elisub()
    def vlad_sub(enrolled_subject):
        return enrolled_subject.sub_1.subjects()
    
class subjects(Subjects):
    def eli_subj(enrolled_subject):
        return subjects()

class vlad:
    def vlad_sub(enrolled_subject):
        return 'IPT-101, MS-102, NET-102, SIA-101'
    
class elisubs:
    def eli_subj(enrolled_subject):
        return'CC-105, IM-101'
class minor:
    def minor_subj(enrolled_subject):
        return 'PE-104, REED4'
print('Major:')
lloyd= vlad()
print(lloyd.vlad_sub())

angelo=elisubs()
print(angelo.eli_subj())

martinez=minor()
print('Minor:')
print(martinez.minor_subj())
