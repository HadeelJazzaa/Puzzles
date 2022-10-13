n=3
matrix=[[0,3,2],
        [3,3,0],
        [1,3,0]]
 
visited=[[False for x in range(n)]
                for y in range(n)]

def ispath(matrix):
    n=len(matrix)
    m=n
    flag=False
     
    for i in range(n):
        for j in range(n):
            if (matrix[i][j]==1)and not visited[i][j]:
                
              flag=checkpath (matrix, i,j)
       
    
    return flag

def checkpath(matrix, i, j):
    flag=False
    
    if (matrix[i][j]== 2):
       
        return True
    if inbourder(matrix,i-1,j) and not visited[i-1][j]:
      up=matrix[i-1][j]
      if (up==3) and up!=0:
        visited[i-1][j]=True  
        checkpath(matrix, i-1, j)
        flag=True
      else:
        flag=False
    
    if inbourder(matrix,i+1,j) and not not visited[i+1][j]:
        down=matrix[i+1][j]
        visited[i+1][j]=True 
        if (down==3) and down!=0:
           checkpath(matrix, i+1, j)
           flag=True
        else:
          flag=False        
    if inbourder(matrix,i,j+1) and not visited[i][j+1]:
        right=matrix[i][j+1]
        visited[i][j+1]
        if (right==3) and right!=0:
           checkpath(matrix, i, j+1)
           flag=True
        else:
          flag=False  
   
   
    if inbourder(matrix,i,j-1) and not visited[i][j-1]:
      left=matrix[i][j-1]
      visited[i][j-1]=True
      if (left==3) and left!=0:
        checkpath(matrix, i, j-1)
        flag=True
      else:
        flag=False
    
          
    return flag  
    
def inbourder(matrix,i,j):
    if (i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])):
       return True  
    return False  






if __name__ =="__main__":
   
    print(ispath(matrix))