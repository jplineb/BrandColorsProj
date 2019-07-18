from torch import nn
from collections import OrderedDict

class ColorNet(nn.Module):
    r"""ColorNet model class -- a simple cnn architecture for predicting color shift masks on input images. 
    
    Args:
        num_filters (int) - number of convolution channels to output from each conv block
        kernel_sizes (2-tuple (int, int)) - kernel sizes for first and last convolutions, respectively
    """

    def __init__(self, num_filters=3, kernel_sizes=(5,3)):

        super(ColorNet, self).__init__()
        
        self.features = nn.Sequential(OrderedDict([
                ('conv0', nn.Conv2d(3, num_filters, kernel_size=kernel_sizes[0], stride=1,
                                    padding=(kernel_sizes[0]-1)//2, bias=False)),
                ('norm0', nn.BatchNorm2d(num_filters)),
                ('relu0', nn.ReLU(inplace=True)),                 
                ('conv1', nn.Conv2d(num_filters, 3, kernel_size=kernel_sizes[1], stride=1,
                                    padding=(kernel_sizes[1]-1)//2, bias=True))    
        ]))

        # Official init from torch repo.
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.constant_(m.bias, 0)

    def forward(self, input):
        return self.features(input)
    
'''
class ResNetBlock(nn.Module):
    r"""Resnet style block for predicting color shift masks on input images. 
    
    Args:
        num_in (int) - number of input channels (and output channels)
        num_features (int) - number of intermediate channels in resnet block
    """

    def __init__(self, num_in, num_features):

        super(ResNetBlock, self).__init__()
        
        self.features = nn.Sequential(OrderedDict([
                            # conv block 1
                            ('conv0', nn.Conv2d(num_in, num_features, kernel_size=3, stride=1,
                                                padding=1, bias=False)),
                            ('norm0', nn.BatchNorm2d(num_features)),
                            ('relu0', nn.ReLU(inplace=True)),
                            # conv block 2
                            ('conv1', nn.Conv2d(num_features, num_in, kernel_size=3, stride=1,
                                                padding=1, bias=False)),
                            ('norm1', nn.BatchNorm2d(num_in)),
                            ('relu1', nn.ReLU(inplace=True))
                        ]))

    def forward(self, input):
        # resnet style output: add input to features
        return intput + self.features(input) 

class ColorResNet(nn.Module):
    r"""ColorResNet model class designed to predict color shift masks on input images. Incorporates resnet-
    style blocks. 
    
    Args:
        num_res_blocks (int) - number of resnet-style bocks 
        num_features_init (int) - number of convolution channels resulting from initial convolution
        num_features_resnets (int) - number of intermediate channels in resnet blocks
    """

    def __init__(self, num_res_blocks=1, num_features_init=16, num_features_resnets=32):

        super(ColorResNet, self).__init__()
        
        # Initial conv
        self.features = nn.Sequential(OrderedDict([
                    ('conv0', nn.Conv2d(3, num_features_init, kernel_size=3, stride=1, #kernelsize originally 7 and padding 3
                                        padding=1, bias=False)),
                    ('norm0', nn.BatchNorm2d(num_features_init)),
                    ('relu0', nn.ReLU(inplace=True))
                ]))
        
        # Resnet blocks
        for i in range(num_res_blocks):
            self.features.add_module('resblock%d' % (i+1), ResNetBlock(num_features_init, num_features_resnets))
            
        # Final output
        self.features.add_module('output', nn.Sequential(OrderedDict([
                    ('conv0', nn.Conv2d(num_features_init, 3, kernel_size=3, stride=1, 
                                        padding=1, bias=False))#,
                    #('norm0', nn.BatchNorm2d(3)),
                    #('relu0', nn.ReLU(inplace=True))
                ])))
            
    def forward(self, input):
        return self.features(input)
    
class ColorNetSimple(nn.Module):
    r"""ColorResNet model class designed to predict color shift masks on input images. Incorporates resnet-
    style blocks. 
    
    Args:
         kernel_size (int) - the size of the convolution kernels. Must be odd.
    """

    def __init__(self, kernel_size=7):

        super(ColorNetSimple, self).__init__()
        
        # Initial conv
        self.features = nn.Sequential(OrderedDict([
                    ('conv0', nn.Conv2d(3, 3, kernel_size=kernel_size, stride=1, 
                                        padding=(kernel_size-1)//2, bias=False)),
                    ('norm0', nn.BatchNorm2d(3)),
                    ('relu0', nn.ReLU(inplace=True))
                ]))
            
    def forward(self, input):
        return self.features(input)'''