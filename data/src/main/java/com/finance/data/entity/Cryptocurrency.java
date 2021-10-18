package com.finance.data.entity;

import lombok.*;

import javax.persistence.*;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.util.Date;

@Entity @Table(name = "cryptocurrency")
@NoArgsConstructor @AllArgsConstructor
@Builder @Setter @Getter @ToString
public class Cryptocurrency {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "cryptocurrency_seq")
    private long cryptoSeq;

    @NotBlank
    @Column(name = "cryptocurrency_code")
    private String cryptoCode;

    @Min(value = 0)
    @Column(name = "cryptocurrency_min_price")
    private long minPrice;

    @Min(value = 0)
    @Column(name = "cryptocurrency_max_price")
    private long maxPrice;

    @Column(name = "standard_date")
    private Date standardDate;

    @Column(name = "update_date")
    private Date updateDate;

    @NotBlank
    @Column(name = "from_data")
    private String fromData;

    @NotNull
    @Transient
    private long timestamp;

}
