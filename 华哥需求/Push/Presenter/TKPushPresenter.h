//
//  TKPushPresenter.h
//  test2
//
//  Created by TryHone on 2017/12/21
//  Copyright © 2017年 TryHone. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "TKPushControllerDelegate.h"

@interface TKPushPresenter : NSObject
-(instancetype)initWithViewDelegate:(id<TKPushViewControllerDelegate>)delegate;
#pragma mark--业务方法
 @end
