from president import President

p = President(26)

print(p.first_name, p.last_name)

attrs = [a for a in dir(p) if not a.startswith('_')]

print(attrs, '\n')

for attr in attrs:
    print(attr, getattr(p, attr))
print()

#  getattr() hasattr() setattr() delattr()

def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "get_full_name", get_full_name)

print(p.get_full_name())

setattr(p, 'assassinated', False)

print(p.assassinated)

def serialize(obj):
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    # ...



