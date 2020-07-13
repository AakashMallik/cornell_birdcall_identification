import torch
from torch.nn.functional import (softmax)
from sklearn.metrics import (roc_auc_score, confusion_matrix)
import matplotlib.pyplot as plt
import seaborn as sn


# def post_process_output(output):
#     # implementation based on problem statement
#     THRESHOLD = 0.5
#     intermediate = torch.sigmoid(output) > THRESHOLD
#     return intermediate.float()

def post_process_output(output):
    # implementation based on problem statement
    return softmax(output, dim=1)

def onehot_converter(V, classes):
    # Create zero vector of desired shape
    OHV = torch.zeros((V.size()[0], classes))

    # Convert from ndarray to array
    V_a = V.view(-1)

    # Fill ones where the label as index
    OHV[range(V.size()[0]), V_a.long()] = 1

    return OHV


# def acc(output_list, target_list):
#     output_list = post_process_output(output_list)
#     I = torch.logical_and(target_list, output_list)
#     U = torch.logical_or(target_list, output_list)
#     batch_iou = torch.sum(I, dim=1, dtype=torch.float)/torch.sum(U, dim=1)
#     acc = torch.sum(batch_iou) / len(batch_iou)
#     return acc.item()

def acc(output_list, target_list):
    acc = torch.argmax(target_list, dim=1).eq(
        torch.argmax(output_list, dim=1))
    return 1.0 * torch.sum(acc.int()).item() / output_list.size()[0]


def f1(output_list, target_list):
    # TODO: Complete implementation
    pass


def aroc(output_list, target_list):
    output_list = post_process_output(output_list)
    target_list = onehot_converter(target_list, output_list.shape[1])
    return roc_auc_score(
        target_list.numpy(),
        output_list.numpy(),
        average="macro"
    )


def confusion_matrix_generator(output_list, target_list, experiment_name):
    output_list = post_process_output(output_list)
    matrix = confusion_matrix(
        torch.argmax(target_list, dim=1).numpy(),
        torch.argmax(output_list, dim=1).numpy()
    )

    labels = ['H', 'MD', 'R', 'S']
    plt.figure()
    figure = sn.heatmap(matrix, xticklabels=labels,
                        yticklabels=labels, annot=True)
    plt.savefig('./results/' + experiment_name + '/confusion_matrix.jpg')
