def runoff(list_voters):
    candidates_set = set()
    for candidate_s_choices in list_voters:
        for choice in candidate_s_choices:
            candidates_set.add(choice)

    if len(candidates_set) == 0:
        return None

    number_of_votes = len(list_voters)
    dic_candidates = {}

    for candidate in candidates_set:
        count = sum(1 for voter in list_voters if voter[0] == candidate)
        dic_candidates[candidate] = count

    winner = max(dic_candidates, key=dic_candidates.get)
    if dic_candidates[winner] > number_of_votes / 2:
        return winner
    lowest_vote = min(dic_candidates.values())
    eliminated_candidates = [candidate for candidate, votes in dic_candidates.items() if votes == lowest_vote]
    if len(eliminated_candidates) == len(candidates_set):
        return None
    for voter in list_voters:
        for eliminated in eliminated_candidates:
            voter.remove(eliminated)
    return runoff(list_voters)


print(runoff([
    ['Lex Luthor', 'Reinhard von Musel', 'Johan Liebert', 'Frank Underwood', 'Abelt Dessler'],
    ['Reinhard von Musel', 'Abelt Dessler', 'Johan Liebert', 'Lex Luthor', 'Frank Underwood'],
    ['Lex Luthor', 'Abelt Dessler', 'Johan Liebert', 'Frank Underwood', 'Reinhard von Musel'],
    ['Reinhard von Musel', 'Frank Underwood', 'Abelt Dessler', 'Lex Luthor', 'Johan Liebert'],
    ['Reinhard von Musel', 'Lex Luthor', 'Abelt Dessler', 'Johan Liebert', 'Frank Underwood'],
    ['Frank Underwood', 'Lex Luthor', 'Johan Liebert', 'Reinhard von Musel', 'Abelt Dessler']
]))  #  None

"""""
print(runoff([
    ['Johan Liebert', 'Daisuke Aramaki', 'Frank Underwood', 'Brian J. Mason', 'Drake Luft', 'Lex Luthor'],
    ['Brian J. Mason', 'Daisuke Aramaki', 'Johan Liebert', 'Frank Underwood', 'Drake Luft', 'Lex Luthor'],
    ['Daisuke Aramaki', 'Johan Liebert', 'Brian J. Mason', 'Drake Luft', 'Lex Luthor', 'Frank Underwood'],
    ['Frank Underwood', 'Brian J. Mason', 'Drake Luft', 'Johan Liebert', 'Lex Luthor', 'Daisuke Aramaki'],
    ['Johan Liebert', 'Drake Luft', 'Lex Luthor', 'Brian J. Mason', 'Frank Underwood', 'Daisuke Aramaki']
]))

print(runoff([["dem", "ind", "rep"],
          ["rep", "ind", "dem"],
          ["ind", "dem", "rep"],
          ["ind", "rep", "dem"]]))
print(runoff([["a", "c", "d", "e", "b"],
            ["e", "b", "d", "c", "a"],
            ["d", "e", "c", "a", "b"],
            ["c", "e", "d", "b", "a"],
            ["b", "e", "a", "c", "d"]]))

print(runoff([['Lex Luthor',        'Drake Luft',           'Reinhard von Musel',   'Abelt Dessler'],
              ['Abelt Dessler',     'Drake Luft',           'Reinhard von Musel',   'Lex Luthor'],
              ['Reinhard von Musel','Drake Luft',           'Lex Luthor',            'Abelt Dessler'],
              ['Lex Luthor',         'Abelt Dessler',       'Drake Luft',              'Reinhard von Musel'],
              ['Reinhard von Musel', 'Lex Luthor',          'Drake Luft',               'Abelt Dessler'],
              ['Abelt Dessler',      'Reinhard von Musel',  'Lex Luthor',               'Drake Luft']]))  # None

print(runoff([['Lex Luthor', 'Reinhard von Musel', 'Johan Liebert', 'Frank Underwood', 'Abelt Dessler'],
        ['Reinhard von Musel', 'Abelt Dessler', 'Johan Liebert', 'Lex Luthor', 'Frank Underwood'],
        ['Lex Luthor', 'Abelt Dessler', 'Johan Liebert', 'Frank Underwood', 'Reinhard von Musel'],
        ['Reinhard von Musel', 'Frank Underwood', 'Abelt Dessler', 'Lex Luthor', 'Johan Liebert'],
        ['Reinhard von Musel', 'Lex Luthor', 'Abelt Dessler', 'Johan Liebert', 'Frank Underwood'],
        ['Frank Underwood', 'Lex Luthor', 'Johan Liebert', 'Reinhard von Musel', 'Abelt Dessler']]))

"""