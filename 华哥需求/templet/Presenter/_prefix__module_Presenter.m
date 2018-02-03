//
//  <prefix><module>Presenter.m
//  test2
//
//  Created by <author> on <time>
//  Copyright © <year>年 <author>. All rights reserved.
//

#import "<prefix><module>Presenter.h"
#import "<prefix><module>ViewControllerDelegate.h"
#import "<prefix><module>ViewModel.h"
@interface <prefix><module>Presenter()
@property(nonatomic,strong) <prefix><module>ViewModel * viewModel;
@end
@implementation <prefix><module>Presenter{
    id<<prefix><module>ViewControllerDelegate> _delegate;
}
-(instancetype)initWithViewDelegate:(id<<prefix><module>ViewControllerDelegate>)delegate{
    self = [super init];
    if (self) {
        _delegate = delegate;
    }
    return self;
}
#pragma mark--业务方法

@end
