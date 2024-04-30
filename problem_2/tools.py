import numpy as np
import matplotlib.pyplot as plt

# generation of matricies

def generate_matrix_simple(nodes = 21 ,connections = [-2,-1,1,2]):
    """
    T matrix for not-disjoint case
    parameter:
        nodes: amount of nodes our networks contains
        connections: array containing the relativ index of neighbours
    return:
        transformation_matrix: T matrix for problem 2
    """
    transformation_matrix = np.zeros((nodes,nodes))
    for i in range(nodes):
        for c in connections:
            transformation_matrix[i,(i+c)%nodes] = 1/len(connections) 
            # % = modulo => generates the periodic boundary conditions
    return transformation_matrix

def generate_matrix_disjoint(sub_nodes = [11,10] ,connections = [-2,-1,1,2]):
    """
    T matrix for disjoint case
    Important Assumption: We assume that both sub network have periodic boundary conditions.
    parameter:
        nodes: amount of nodes each subnet contains
        connections: array containing the relativ index of neighbours
    return:
        transformation_matrix: T matrix for problem 2
    """
    # we assume that each subnet is the same as the network from a, but with different nodes
    sub_net_matricies = []
    for nodes in sub_nodes:
        sub_net_matricies.append(generate_matrix_simple(nodes,connections))
    
    # transform for numpy block
    block_matrix_form = []
    for i, sub_net_m_1 in enumerate(sub_net_matricies):
        block_matrix_form.append([])
        for j, sub_net_m_2 in enumerate(sub_net_matricies):
            if i == j:
                block_matrix_form[i].append(sub_net_m_1)
            else: 
                block_matrix_form[i].append(np.zeros((sub_net_m_1.shape[1],sub_net_m_2.shape[0])))

    transformation_matrix = np.block(block_matrix_form)

    return transformation_matrix


# generation of inital vectors 

def inital_state_delta(nodes=21,delta_x = 10):
    """
    creates an inital state vector with all the charge located in one point
    parameter:
        nodes: amount of nodes of the network
        delta_x: poision of the inital charge 
    return:
        inital_vector
    """
    inital_vector = np.zeros(nodes)
    inital_vector[delta_x] = 1
    return inital_vector

def inital_state_random(nodes=21,):
    """
    creates an intial state vector with random starting conditions, but normalized on 1
    parameter:
        nodes: amount of nodes of the network
    return:
        inital_vector
    """
    inital_vector = np.random.rand(21)
    inital_vector /= np.sum(inital_vector)
    return inital_vector

def inital_state_task_f(nodes=21):
    """
    creates an inital state vector according to task f
    parameter:
        nodes: amount of nodes of the network
        delta_x: poision of the inital charge 
    return:
        inital_vector
    """
    inital_vector = np.zeros(nodes)
    for i in range(len(inital_vector)):
        inital_vector[i] = 1/(i+1)
    return inital_vector


# simulating the system

def simulate(matrix,inital_vector,steps):
    """
    iterates 'steps'-time the system and saves all steps
    parameter:
        matrix: this is our transformation_matrix
        inital_vector: starting vector
        steps: amout of iterative steps
    return:
        time_development: 
    """
    time_development = [inital_vector,]
    vector = inital_vector
    for step in range(steps):
        vector = np.dot(matrix,vector)
        time_development.append(vector)
    return time_development



# Finding eigenvalues


def power_iteration(matrix, maxiter = 1000, tol = 1e-3):
    """
    power_interation, was the introduced method in the lectures and this function is orientated/taken from the accompyning github: https://github.com/nordam/ComputationalPhysics/blob/master/Notebooks/11%20-%20Eigenvalues%2C%20eigenvectors%20and%20SVD.ipynb
    parameter: 
        matrix: matrix, for which we want to find eigenvalue and vector
        maxiter: maximum amount of iterations
        tol: tolerance for convergence
    returns:
        eigval, eigvec, conv_status
        status: True(converged)/False(did not converge in our tolerance)
    """
    
    # Start with a random vector. It is quite unlikely that this
    # will be exactly orthogonal to the desired eigenvector
    b0 = np.random.rand(matrix.shape[1])
    # normalise vector
    b0 = b0 / np.linalg.norm(b0)
    
    for i in range(maxiter):
        # Calculate product
        b1 = np.dot(matrix,b0)
        # Calculate "stretch" factor
        b1_norm = np.linalg.norm(b1)
        # Normalise vector
        b1 = b1 / b1_norm
        # check for convergence
        if np.linalg.norm(b1 - b0) < tol:
            return b1_norm, b1, False
        else:
            # Continue iterations
            b0 = b1
    # If we arrived here, iterations did not converge
    return b1_norm, b1, True




if __name__ == "__main__":
    # debug 
    print(inital_state_delta())
    print(inital_state_task_f())

