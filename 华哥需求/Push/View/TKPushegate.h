//
//  TKPushViewControllerDelegate.h
//  test2
//
//  Created by TryHone on 2017/12/21
//  Copyright © 2017年 TryHone. All rights reserved.
//

#ifndef TKPushViewControllerDelegate_h
#define TKPushViewControllerDelegate_h

@protocol TKPushViewControllerDelegate <NSObject>
@optional
- (void)refresh:(NSString *)key data:(id)data;
@end
#endif
