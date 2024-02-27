from typing import List, Tuple
import pandas as pd

def sb_tree(rn: List[Tuple[int, int]], n: int) -> List[Tuple[int, int]]:
    """
    Generate the Stern-Brocot tree up to level n.
    
    Parameters:
    rn (List[Tuple[int, int]]): The initial fractions [(0, 1), (1, 0)].
    n (int): The desired level to generate the tree up to.
    
    Returns:
    List[Tuple[int, int]]: The Stern-Brocot tree up to level n.
    """
    if not n:
        return rn
    def new_rn():
        for i in range(len(rn) - 1):
            yield from (rn[i], tuple(map(sum, zip(rn[i], rn[i+1]))))
        yield rn[i+1]
    return sb_tree(list(new_rn()), n-1)

def format_tree(tree: List[List[Tuple[int, int]]]) -> List[List[str]]:
    """
    Format the Stern-Brocot tree to display fractions.
    
    Parameters:
    tree (List[List[Tuple[int, int]]]): The generated Stern-Brocot tree.
    
    Returns:
    List[List[str]]: The formatted Stern-Brocot tree with fractions as strings.
    """
    return [[f"{num}/{den}" for num, den in level] for level in tree]

def unique_in_level(formatted_tree: List[List[str]]) -> List[List[str]]:
    """
    Extract unique fractions introduced at each level of the Stern-Brocot tree.
    
    Parameters:
    formatted_tree (List[List[str]]): The formatted Stern-Brocot tree with fractions as strings.
    
    Returns:
    List[List[str]]: Unique fractions introduced at each level.
    """
    unique_fractions = []
    seen = set()
    for level in formatted_tree:
        new_level = []
        for frac in level:
            if frac not in seen:
                seen.add(frac)
                new_level.append(frac)
        unique_fractions.append(new_level)
    return unique_fractions

# Example usage to generate and format the Stern-Brocot tree for 5 levels
tree = [list(sb_tree([(0, 1), (1, 0)], i)) for i in range(6)]  # Generate tree up to level 5
formatted_tree = format_tree(tree)  # Format the tree with fractions as strings
unique_fractions = unique_in_level(formatted_tree)  # Extract unique fractions for each level

# Display the unique fractions for each level (for demonstration)
for i, level in enumerate(unique_fractions, 1):
    print(f"Level {i}: {', '.join(level)}")
