from const import *
from trainers import *
from utils import Data
import pickle
data = Data()


class CnnExp():
    def __init__(self) -> None:
        # self.datasets = BIG
        # self.data = Data()
        pass

    def debug(self, dataset=MNIST, tag=BAYES):
        print(dataset, tag)
        trainer = Trainer(dataset)
        if tag == "resnet18":
            trainer.train("resnet18")
        elif tag == "resnet34":
            trainer.reset_model([64, 128, 256, 512, 3, 4, 6, 3])
            trainer.train("resnet34")
        else:
            with open(f"hparams/{dataset}_{tag}.json", "r") as f:
                hparams = json.load(f)
            trainer.reset_model(hparams)
            trainer.train(tag)
        return

    def cal_hparams(self, dataset=MNIST):
        print(dataset)
        trainer = Trainer(dataset)
        print("bayes")
        trainer.bayes()
        print("zoopt")
        trainer.zoopt()
        print("rand")
        trainer.rand()
        print("ga")
        trainer.ga()
        print("pso")
        trainer.pso()
        print("hb")
        trainer.hyper_band()
        print("dehb")
        trainer.dehb()
        return

    def generate_sample_for_mehp(self, dataset):
        trainer = Trainer(dataset)
        print(dataset)
        trainer.generate_training_sample()
        return

    def train_mehp(self, dataset):
        trainer = Trainer(dataset)
        trainer.train_mapper()
        return

    def cal_params_for_mehp(self, dataset):
        print(dataset)
        trainer = Trainer(dataset)
        st = time.time()
        train_embedding = trainer.embedding_dataset(trainer.train_loader)
        mapper = Mapper()
        mapper.load_state_dict(torch.load(f'mehp/{dataset}_model'))
        hps = mapper(torch.Tensor(train_embedding).unsqueeze(0))
        hps = mapper.generate(hps)
        hps = hps.squeeze(0)
        print(time.time() - st)
        print(hps)
        return


if __name__ == "__main__":
    exp = CnnExp()
    # # formal run for mdhp
    # exp.debug(MNIST, MEHP)
    # exp.debug(SVHN, MEHP)
    # exp.debug(CIFAR10, MEHP)
    # exp.debug(CIFAR100, MEHP)

    # # calculate h-parameters for mdhp
    # exp.cal_params_for_mehp(MNIST)
    # exp.cal_params_for_mehp(SVHN)
    # exp.cal_params_for_mehp(CIFAR10)
    # exp.cal_params_for_mehp(CIFAR100)

    # # train mapper
    # exp.train_mehp(MNIST)
    # exp.train_mehp(SVHN)
    # exp.train_mehp(CIFAR10)
    # exp.train_mehp(CIFAR100)

    # make data
    # exp.generate_sample_for_mehp(MNIST)
    # exp.generate_sample_for_mehp(SVHN)
    # exp.generate_sample_for_mehp(CIFAR10)
    exp.generate_sample_for_mehp(CIFAR100)

    # # calculate h-parameters of baselines
    # exp.cal_hparams(MNIST)
    # exp.cal_hparams(SVHN)
    # exp.cal_hparams(CIFAR10)
    # exp.cal_hparams(CIFAR100)

    # # formal running
    # exp.debug(MNIST, "resnet34")
    # for dataset in [CIFAR100]:
    #     exp.debug(dataset, BAYES)
    #     exp.debug(dataset, GENETICA)
    #     exp.debug(dataset, HYPERBAND)
    #     exp.debug(dataset, PARTICLESO)
    #     exp.debug(dataset, RAND)
    #     exp.debug(dataset, ZOOPT)
    #     exp.debug(dataset, DEHBCONST)
    #     # exp.debug(dataset, "resnet18")
    #     # exp.debug(dataset, "resnet34")
pass
