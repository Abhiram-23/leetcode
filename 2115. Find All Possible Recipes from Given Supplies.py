# class Solution:
#     def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#         suppelies = set(supplies)
#         k = set(recipes)
#         res = set()
#         left = []
#         for i in range(len(recipes)):
#             c = True
#             for j in range(len(ingredients[i])):
#                 # print(ingredients[i][j]) 
#                 if ingredients[i][j] not in supplies and ingredients[i][j] not in res:
#                     c = False
#                     left.append(i)
#                     break
#             if c:
#                 res.add(recipes[i])
#         # print(left)
#         for i in range(len(left)):
#             for j in range(len(ingredients[left[i]])):
#                 c = True
#                 if ingredients[left[i]][j] not in supplies and ingredients[left[i]][j] not in res:
#                     c = False
#                     left.append(i)
#                     break
#             if c:
#                 res.add(recipes[i])
#         return list(res)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_supplies = set(supplies)
        
        recipe_to_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        
        visited = {}
        result = []
        
        def can_make(recipe):
            if recipe in visited and visited[recipe] == 0:
                return False
                
            if recipe in visited and visited[recipe] == 1:
                return True
                
            if recipe in available_supplies:
                return True
                
            if recipe not in recipe_to_ingredients:
                return False
                
            visited[recipe] = 0
            
            for ingredient in recipe_to_ingredients[recipe]:
                if not can_make(ingredient):
                    visited[recipe] = -1
                    return False
                    
            visited[recipe] = 1
            result.append(recipe)
            return True
        
        for recipe in recipes:
            can_make(recipe)
        
        return [recipe for recipe in recipes if recipe in visited and visited[recipe] == 1]
        