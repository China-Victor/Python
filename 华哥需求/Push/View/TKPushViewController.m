//
//  TKPushViewController.m
//  test2
//
//  Created by TryHone on 2017/12/21
//  Copyright © 2017年 TryHone. All rights reserved.
//

#import "TKPushViewController.h"


@interface  TKPushViewController ()< TKPushViewControllerDelegate>
@end

@implementation TKPushViewController
#pragma mark--生命周期
- (void)loadView {
    [super loadView];
}
- (void)viewDidLoad {
    [super viewDidLoad];
}
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
}
- (void)viewWillDisappear:(BOOL)animated {
    [super viewWillDisappear:animated];
}
- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
}
-(void)dealloc{
}
#pragma mark-属性设置

#pragma mark--页面事件

#pragma mark--tableview代理事件

#pragma mark--事件路由
-(void)routerEventWithName:(NSString *)eventName userInfo:(NSObject *)userInfo
{

}

#pragma mark--TKPushViewControllerDelegate
-(void)refresh:(NSString *)key data:(id)data{

}
#pragma mark--空数据带来

#pragma mark--懒加载

@end
