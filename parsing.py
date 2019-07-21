''' Utils for parsing raw recipe data '''

from lark import Lark, Transformer
import pprint

def list_from_file(path):
    lst = []
    with open(path) as f:
        for line in f:
            string = line.strip()
            if len(string) > 0:
                lst.append(string)
    return lst

def list_to_grammar(lst):
    ''' converts list of string into valid grammar string e.g ["a","b","c"] --> "a"|"b"|"c" '''
    strs = ['"{}"'.format(x) for x in lst]
    return "|".join(strs)



standard_units = list_from_file('data/standard-units.txt')

_GRAMMAR_ =  '''
?start: ingredient

ingredient: quantity? unit? base_ingredient

quantity.2: mixed_fraction | fraction | number

mixed_fraction: number fraction
fraction: number "/" number

unit: standard_unit | non_standard_unit

standard_unit.2: standard_unit_plural | STANDARD_UNIT_NAME
?standard_unit_plural.2: STANDARD_UNIT_NAME ("es" | "s")
STANDARD_UNIT_NAME: {standard_units}  

non_standard_unit.2: unit_size?  (non_standard_unit_plural | NON_STANDARD_UNIT_NAME)
?non_standard_unit_plural.2: NON_STANDARD_UNIT_NAME ("es" | "s")
NON_STANDARD_UNIT_NAME: "can" | "jar"
unit_size: "(" quantity standard_unit ")"

base_ingredient.0: WORD+

number: NUMBER
WORD: /[A-Za-z]+/

%import common.NUMBER 
%import common.WS
%ignore WS

'''.format(standard_units=list_to_grammar(standard_units))

parser = Lark(_GRAMMAR_)


class IngredientTransformer(Transformer):
    def fraction(self, children):
        return float(children[0]) / float(children[1])
    
    def mixed_fraction(self, children):
        return float(children[0]) + children[1]
        
    def number(self, children):
        return float(children[0])
    
    def decimal(self, children):
        return float(children[0])
    
    
    def standard_unit(self,children):
        return {"type":"standard", "name": children[0].value}
    

    def ingredient(self, children):
        result = {}
        for child in children:
            if child.data == "quantity":
                result['quantity'] = child.children[0]
            if child.data == "unit":
                result['unit'] = child.children[0]
            if child.data == "base_ingredient":
                result["base_ingredient"] = " ".join([x.value for x in child.children])
        
        return result
    


def parse_ingredient(string):
    ''' parses ingredient to structured dict '''
    tree = parser.parse(string)
    return IngredientTransformer().transform(tree)


if __name__ == "__main__":
    tree = parser.parse("1 1/2 cup whole grain flour")
    print(tree)
    print(tree.pretty())
    tree = IngredientTransformer().transform(tree)
    pprint.pprint(tree)