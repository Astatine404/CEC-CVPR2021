import numpy as np
import torch
from dataloader.sampler import CategoriesSampler
from dataloader.datasets import *

def set_up_datasets(args):
    if args.dataset == 'cifar100':
        import dataloader.cifar100.cifar as Dataset
        args.base_class = 60
        args.num_classes=100
        args.way = 5
        args.shot = 5
        args.sessions = 9
    if args.dataset == 'cub200':
        import dataloader.cub200.cub200 as Dataset
        args.base_class = 100
        args.num_classes = 200
        args.way = 10
        args.shot = 5
        args.sessions = 11
    if args.dataset == 'mini_imagenet':
        import dataloader.miniimagenet.miniimagenet as Dataset
        args.base_class = 60
        args.num_classes=100
        args.way = 5
        args.shot = 5
        args.sessions = 9
    args.Dataset=Dataset
    return args

def get_dataloader(args,session):
    if session == 0:
        trainset, trainloader, testloader = get_base_dataloader(args)
    else:
        trainset, trainloader, testloader = get_new_dataloader(args)
    return trainset, trainloader, testloader

def get_base_dataloader(args):
    txt_path = "data/index_list/" + args.dataset_dir + "/session_" + str(0 + 1) + '.txt'
    class_index = np.arange(args.base_class)
    target_transform = None
    if args.dataset == 'cifar100':
        if args.dataset_type == 'biased':
            class_index = custom_base_classes
            target_transform = lambda target: class_map[target]
        elif args.dataset_type == 'random':
            class_index = custom_base_classes_random
            target_transform = lambda target: class_map_random[target]
            if args.dataset_dir == 'random_1':
                class_index = custom_base_classes_random_1
                target_transform = lambda target: class_map_random_1[target]
            elif args.dataset_dir == 'random_2':
                class_index = custom_base_classes_random_2
                target_transform = lambda target: class_map_random_2[target]
        elif args.dataset_type == 'superrandom':
            if args.dataset_dir == 'superrandom_1':
                class_index = custom_base_classes_superrandom_1
                target_transform = lambda target: class_map_superrandom_1[target]
            elif args.dataset_dir == 'superrandom_2':
                class_index = custom_base_classes_superrandom_2
                target_transform = lambda target: class_map_superrandom_2[target]
            elif args.dataset_dir == 'superrandom_5':
                class_index = custom_base_classes_superrandom_5
                target_transform = lambda target: class_map_superrandom_5[target]

        trainset = args.Dataset.CIFAR100(root=args.dataroot, train=True, download=True,
                                         index=class_index, base_sess=True, target_transform=target_transform)
        testset = args.Dataset.CIFAR100(root=args.dataroot, train=False, download=False,
                                        index=class_index, base_sess=True, target_transform=target_transform)

    if args.dataset == 'cub200':
        trainset = args.Dataset.CUB200(root=args.dataroot, train=True,
                                       index=class_index, base_sess=True)
        testset = args.Dataset.CUB200(root=args.dataroot, train=False, index=class_index)

    if args.dataset == 'mini_imagenet':
        trainset = args.Dataset.MiniImageNet(root=args.dataroot, train=True,
                                             index=class_index, base_sess=True)
        testset = args.Dataset.MiniImageNet(root=args.dataroot, train=False, index=class_index)


    trainloader = torch.utils.data.DataLoader(dataset=trainset, batch_size=args.batch_size_base, shuffle=True,
                                              num_workers=8, pin_memory=True)
    testloader = torch.utils.data.DataLoader(
        dataset=testset, batch_size=args.test_batch_size, shuffle=False, num_workers=8, pin_memory=True)

    return trainset, trainloader, testloader



def get_base_dataloader_meta(args):
    txt_path = "data/index_list/" + args.dataset + "/session_" + str(0 + 1) + '.txt'
    class_index = np.arange(args.base_class)
    if args.dataset == 'cifar100':
        trainset = args.Dataset.CIFAR100(root=args.dataroot, train=True, download=True,
                                         index=class_index, base_sess=True)
        testset = args.Dataset.CIFAR100(root=args.dataroot, train=False, download=False,
                                        index=class_index, base_sess=True)

    if args.dataset == 'cub200':
        trainset = args.Dataset.CUB200(root=args.dataroot, train=True,
                                       index_path=txt_path)
        testset = args.Dataset.CUB200(root=args.dataroot, train=False,
                                      index=class_index)
    if args.dataset == 'mini_imagenet':
        trainset = args.Dataset.MiniImageNet(root=args.dataroot, train=True,
                                             index_path=txt_path)
        testset = args.Dataset.MiniImageNet(root=args.dataroot, train=False,
                                            index=class_index)


    # DataLoader(test_set, batch_sampler=sampler, num_workers=8, pin_memory=True)
    sampler = CategoriesSampler(trainset.targets, args.train_episode, args.episode_way,
                                args.episode_shot + args.episode_query)

    trainloader = torch.utils.data.DataLoader(dataset=trainset, batch_sampler=sampler, num_workers=args.num_workers,
                                              pin_memory=True)

    testloader = torch.utils.data.DataLoader(
        dataset=testset, batch_size=args.test_batch_size, shuffle=False, num_workers=args.num_workers, pin_memory=True)

    return trainset, trainloader, testloader

def get_new_dataloader(args,session):
    txt_path = "data/index_list/" + args.dataset_dir + "/session_" + str(session + 1) + '.txt'
    target_transform = None
    if args.dataset == 'cifar100':
        if args.dataset_type == 'biased':
            txt_path = "data/index_list/biased/" + args.dataset + "/session_" + str(session + 1) + '.txt'
            target_transform = lambda target: class_map[target]
        elif args.dataset_type == 'random':
            txt_path = "data/index_list/" + args.dataset_dir + "/session_" + str(session + 1) + '.txt'
            target_transform = lambda target: class_map_random[target]
            if args.dataset_dir == 'random_1':
                class_index = custom_base_classes_random_1
                target_transform = lambda target: class_map_random_1[target]
            elif args.dataset_dir == 'random_2':
                class_index = custom_base_classes_random_2
                target_transform = lambda target: class_map_random_2[target]
        elif args.dataset_type == 'superrandom':
            if args.dataset_dir == 'superrandom_1':
                class_index = custom_base_classes_superrandom_1
                target_transform = lambda target: class_map_superrandom_1[target]
            elif args.dataset_dir == 'superrandom_2':
                class_index = custom_base_classes_superrandom_2
                target_transform = lambda target: class_map_superrandom_2[target]
            elif args.dataset_dir == 'superrandom_5':
                class_index = custom_base_classes_superrandom_5
                target_transform = lambda target: class_map_superrandom_5[target]
        class_index = open(txt_path).read().splitlines()
        trainset = args.Dataset.CIFAR100(root=args.dataroot, train=True, download=False,
                                         index=class_index, base_sess=False, target_transform=target_transform)
    if args.dataset == 'cub200':
        trainset = args.Dataset.CUB200(root=args.dataroot, train=True,
                                       index_path=txt_path)
    if args.dataset == 'mini_imagenet':
        trainset = args.Dataset.MiniImageNet(root=args.dataroot, train=True,
                                       index_path=txt_path)
    if args.batch_size_new == 0:
        batch_size_new = trainset.__len__()
        trainloader = torch.utils.data.DataLoader(dataset=trainset, batch_size=batch_size_new, shuffle=False,
                                                  num_workers=args.num_workers, pin_memory=True)
    else:
        trainloader = torch.utils.data.DataLoader(dataset=trainset, batch_size=args.batch_size_new, shuffle=True,
                                                  num_workers=args.num_workers, pin_memory=True)

    # test on all encountered classes
    class_new = get_session_classes(args, session)

    if args.dataset == 'cifar100':
        testset = args.Dataset.CIFAR100(root=args.dataroot, train=False, download=False,
                                        index=class_new, base_sess=False, target_transform=target_transform)
    if args.dataset == 'cub200':
        testset = args.Dataset.CUB200(root=args.dataroot, train=False,
                                      index=class_new)
    if args.dataset == 'mini_imagenet':
        testset = args.Dataset.MiniImageNet(root=args.dataroot, train=False,
                                      index=class_new)

    testloader = torch.utils.data.DataLoader(dataset=testset, batch_size=args.test_batch_size, shuffle=False,
                                             num_workers=args.num_workers, pin_memory=True)

    return trainset, trainloader, testloader

def get_session_classes(args,session):
    class_list=np.arange(args.base_class + session * args.way)
    if args.dataset_type == 'biased':
        class_list = custom_base_classes.copy()
        for sess in range(session):
            class_list += custom_inc_classes[sess]
    elif args.dataset_type == 'random':
        class_list = custom_base_classes_random.copy()
        for sess in range(session):
            class_list += custom_inc_classes_random[sess]
        
        if args.dataset_dir == 'random_1':
            class_list = custom_base_classes_random_1.copy()
            for sess in range(session):
                class_list += custom_inc_classes_random_1[sess]
        elif args.dataset_dir == 'random_2':
            class_list = custom_base_classes_random_2.copy()
            for sess in range(session):
                class_list += custom_inc_classes_random_2[sess]
    elif args.dataset_type == 'superrandom':
        if args.dataset_dir == 'superrandom_1':
            class_list = custom_base_classes_superrandom_1.copy()
            for sess in range(session):
                class_list += custom_inc_classes_superrandom_1[sess]
        elif args.dataset_dir == 'superrandom_2':
            class_list = custom_base_classes_superrandom_2.copy()
            for sess in range(session):
                class_list += custom_inc_classes_superrandom_2[sess]
        elif args.dataset_dir == 'superrandom_5':
            class_list = custom_base_classes_superrandom_5.copy()
            for sess in range(session):
                class_list += custom_inc_classes_superrandom_5[sess]
                
    return class_list