//
//  TKPushPresenter.m
//  test2
//
//  Created by TryHone on 2017/12/21
//  Copyright © 2017年 TryHone. All rights reserved.
//

#import "TKPushPresenter.h"
#import "TKPushViewControllerDelegate.h"
#import "TKPushViewModel.h"
@interface TKPushPresenter()
@property(nonatomic,strong) TKPushViewModel * viewModel;
@end
@implementation TKPushPresenter{
    id<TKPushViewControllerDelegate> _delegate;
}
-(instancetype)initWithViewDelegate:(id<TKPushViewControllerDelegate>)delegate{
    self = [super init];
    if (self) {
        _delegate = delegate;
    }
    return self;
}
#pragma mark--业务方法

@end
