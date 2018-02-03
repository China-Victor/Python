//
//  <prefix><module>ViewController.m
//  test2
//
//  Created by <author> on <time>
//  Copyright © <year>年 <author>. All rights reserved.
//

#import "<prefix><module>ViewController.h"


@interface  <prefix><module>ViewController ()< <prefix><module>ViewControllerDelegate>
@end

@implementation <prefix><module>ViewController
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

#pragma mark--<prefix><module>ViewControllerDelegate
-(void)refresh:(NSString *)key data:(id)data{

}
#pragma mark--空数据带来

#pragma mark--懒加载

@end
