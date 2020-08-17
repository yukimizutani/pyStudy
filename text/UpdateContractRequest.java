package com.kinto.web.model.member;

import com.kinto.web.core.undefined.InitialUndefinedValue;

import lombok.Data;
import lombok.EqualsAndHashCode;

/**
 * 中途解約情報更新用APIリクエスト
 *
 * @author ryoKusuki
 *
 */
@Data
@EqualsAndHashCode(callSuper = false)
public class UpdateCancellationRequest extends InitialUndefinedValue {
  private String contractId;
  private String updateUser;
  private String updateDatetime;
  private CancellationModel cancellation;

  /**
   * 中途解約情報
   */
  @Data
  @EqualsAndHashCode(callSuper = false)
  public static class CancellationModel extends InitialUndefinedValue {
    private Integer cancellationStatusSv;
    private Integer cancellationReasonSv;
    private String cancellationReasonOther;
    private String cancellationRequestedDate;
  }

}
